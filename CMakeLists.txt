cmake_minimum_required(VERSION 3.0)
project(python_native_boilerplate)

find_package(
  Python3
  COMPONENTS Interpreter Development
  REQUIRED)
include_directories(${Python3_INCLUDE_DIRS})

set(BINDING_FILES src/native/bindings/example_module.c)
set(HEADER_FILES include/native/example.h)
set(SOURCE_FILES src/native/example.c)

set(CMAKE_SHARED_LIBRARY_PREFIX "_")
set(CMAKE_STATIC_LIBRARY_PREFIX "_")

add_library(example SHARED ${SOURCE_FILES} ${HEADER_FILES} ${BINDING_FILES})

target_link_libraries(example Python3::Python)
