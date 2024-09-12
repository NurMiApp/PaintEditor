cmake_minimum_required(VERSION 3.10)
project(PaintApp)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Find SFML
# Assuming SFML is installed in a standard location
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)

# Add the executable
add_executable(PaintApp main.cpp)

# Link SFML libraries
target_link_libraries(PaintApp sfml-graphics sfml-window sfml-system)
