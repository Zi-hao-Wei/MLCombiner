#include "llvm/IR/PassManager.h"
#include "llvm/Passes/PassBuilder.h"
#include "llvm/Passes/PassPlugin.h"
#include "llvm/Support/raw_ostream.h"

#include <iostream>
#include <cstring>
#include <unordered_map>

using namespace llvm;

namespace {

struct inputter : public PassInfoMixin<inputter> {

    PreservedAnalyses run(Function &F, FunctionAnalysisManager &FAM) {
        // for (auto &BB : F){
        //     for(auto &I : BB){
        //         errs() << I << "\n";
        //     }
        // }
        errs() << "Function: "<<F.getName()<< "\n";
        std::unordered_map<std::string, int> tracker;
        int counterB = 1;
        for (auto &BB : F){
            int counter = 1;
            errs() << "[BB"<<counterB << "]\n";
            // bool flag = false;
            for(auto &I : BB){
                errs() << "[Original]I"<<counter<<":"<<I << "\n";
                std::string str;
                llvm::raw_string_ostream ss(str);
                ss << I;
                std::string temp = "";
                std::vector<std::string> total;
                for(int i=0; i<(int)str.size(); i++){
                    if(ss.str()[i] != ' '&& ss.str()[i] !=','){
                        temp += ss.str()[i];
                    }else{
                        if(temp.size()!=0){
                            // errs() << "hello: "<<temp << "\n";
                            if(temp != "=" ){
                                if(temp != "i32"&&temp != "i64")
                                    for (auto & c: temp) c = toupper(c);
                                total.push_back(temp);
                            }else{
                                // flag = true;
                                // errs() << "add "<<total.back()<<"\n";
                                tracker[total.back()] = counter;
                                total.pop_back();
                            }
                            temp = "";
                        }
                        
                    }
                }
                for (auto & c: temp) c = toupper(c);
                total.push_back(temp);
                errs() << "[Encoded] I"<<counter <<": ";
                counter++;
                std::string data;
                for(int i=0; i<(int)total.size(); i++){
                    // errs()  << "\ntotal[i]="<< total[i];
                    if(total[i][0] == '%'){
                        int index = 0;
                        for(index;index<(int)total[i].size(); index++){
                            if(isdigit(total[i][index])||total[i][index] == '%'){
                                data+=total[i][index];
                            }
                        }
                        // errs()  << "Changing... "<< data;
                        if(tracker.find(data)!= tracker.end())
                        {
                            std::string change = ")"+ total[i].substr(index, total[i].size()-index);
                            total[i] = "(I"+std::to_string(tracker[data])+ change;
                            
                            // errs() << " to "<<total[i]<<"\n";
                            // errs() <<"(I"<<tracker[data]<< change <<"\n";
                        } 
                        data = "";     
                    }else{
                        // errs() << total[i] << " ";
                    }
                    
                }
                for(int i=0; i<(int)total.size(); i++){
                    errs() << total[i] << " ";
                }
                errs()<< "\n";
                // errs() << ss.str() << "\n";

                // for (int p = 0; p<I.getNumOperands(); p++){
                //     // if (auto *producer = I.getOperand(p)->getDefiningOp()) {
                //     //     errs() << "  - Operand produced by operation '"<< producer->getName() << "'\n";
                //     // }
                //     errs() << I.getOperand(p)->getName() << "\n";
                // }
            }
            counterB++;
        }
        return PreservedAnalyses::all();
    }
};
}

extern "C" ::llvm::PassPluginLibraryInfo LLVM_ATTRIBUTE_WEAK llvmGetPassPluginInfo() {
    return {
        LLVM_PLUGIN_API_VERSION, "inputter", "v0.1",
        [](PassBuilder &PB) {
            PB.registerPipelineParsingCallback(
                [](StringRef Name, FunctionPassManager &FPM,
                ArrayRef<PassBuilder::PipelineElement>) {
                    if(Name == "inputter"){
                        FPM.addPass(inputter());
                        return true;
                    }
                    return false;
                }
            );
        }
     };
}