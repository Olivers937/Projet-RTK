# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\module_core_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\module_core_autogen.dir\\ParseCache.txt"
  "module_core_autogen"
  )
endif()
