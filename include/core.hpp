#ifndef CORE_HPP
#define CORE_HPP

#include <iostream>
#include <vector>
#include <array>

#include "Path.hpp"
#include "User.hpp"
#include "Circle.hpp"

#include "types/Obstacle.hpp"

class Core {
    User m_user;
    Path m_path;
    std::vector<ObstacleData> m_obstacle_datas = {};
    int m_path_design_index_dt = 100;

public:
    // Constructors
    Core() = delete;
    Core(User user, Path path);

    // Accessors
    int path_design_dt() const noexcept { return m_path_design_index_dt; };

    // Member functions
    void set_obstacles_datas(std::vector<ObstacleData> obstacle_datas);
    bool check_obstacles() const noexcept;
    bool user_exceed_path() const noexcept;
    void design_path() noexcept;
};

#endif // !CORE_HPP