#include "Core.hpp"

Core::Core(User user, Path path)
    : m_user(user), m_path(path) {}

/**
 * @brief Setter for m_obstacle_datas field
 */
void Core::set_obstacles_datas(std::vector<ObstacleData> obstacle_datas){
    m_obstacle_datas = obstacle_datas;
}

/**
 * @brief Detects if an obstacle is reported by the obstacle detection module
 */
bool Core::check_obstacles() const noexcept {
    return std::size(m_obstacle_datas) > 0;
}

/**
 * @brief Check if the user has exceeded the path given in order to draw a new path
 */
bool Core::user_exceed_path() const noexcept {
    Circle user_circle { m_user.get_circle() };
    std::vector<GPSCoords> points { m_path.points() };

    std::vector<GPSCoords>::iterator it { std::begin(points) };

    for(; it != std::end(points); it++) {
        if (user_circle.contains(*it)) {
            return false;
        }
    }

    return true;
}

/**
 * @brief Creates a new short path segment starting from the user's current position and connects it to the original path.
 */
void Core::design_path() noexcept {
    std::vector<GPSCoords> original_path { m_path.points() };

    int actual_index { m_path.actual_index() };
    int forward_index { actual_index + m_path_design_index_dt };
    
    GPSCoords actual_point { m_path.get_point(actual_index) };
    GPSCoords forward_point { m_path.get_point(forward_index) };
    
    std::vector<GPSCoords> new_path { Path::construct_path(actual_point, forward_point) };

    std::copy(new_path.begin(), new_path.end(), original_path.begin() + actual_index);
    
    m_path.points(original_path);
}