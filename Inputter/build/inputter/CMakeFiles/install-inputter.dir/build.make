# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ellenai/hw0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ellenai/hw0/build

# Utility rule file for install-inputter.

# Include any custom commands dependencies for this target.
include inputter/CMakeFiles/install-inputter.dir/compiler_depend.make

# Include the progress variables for this target.
include inputter/CMakeFiles/install-inputter.dir/progress.make

inputter/CMakeFiles/install-inputter:
	cd /home/ellenai/hw0/build/inputter && /usr/bin/cmake -DCMAKE_INSTALL_COMPONENT="inputter" -P /home/ellenai/hw0/build/cmake_install.cmake

install-inputter: inputter/CMakeFiles/install-inputter
install-inputter: inputter/CMakeFiles/install-inputter.dir/build.make
.PHONY : install-inputter

# Rule to build all files generated by this target.
inputter/CMakeFiles/install-inputter.dir/build: install-inputter
.PHONY : inputter/CMakeFiles/install-inputter.dir/build

inputter/CMakeFiles/install-inputter.dir/clean:
	cd /home/ellenai/hw0/build/inputter && $(CMAKE_COMMAND) -P CMakeFiles/install-inputter.dir/cmake_clean.cmake
.PHONY : inputter/CMakeFiles/install-inputter.dir/clean

inputter/CMakeFiles/install-inputter.dir/depend:
	cd /home/ellenai/hw0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ellenai/hw0 /home/ellenai/hw0/inputter /home/ellenai/hw0/build /home/ellenai/hw0/build/inputter /home/ellenai/hw0/build/inputter/CMakeFiles/install-inputter.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : inputter/CMakeFiles/install-inputter.dir/depend
