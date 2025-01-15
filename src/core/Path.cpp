#include "Path.hpp"

Path::Path(GPSCoords start_point, GPSCoords end_point) {
    m_points = construct_path(start_point, end_point);
    m_actual_index = 0;
}

// TODO
std::vector<GPSCoords> Path::construct_path(GPSCoords start_point, GPSCoords end_point) {
    return {};
};

/**
 * @brief Get the corresponding point to an index
 */
GPSCoords Path::get_point(int index) const noexcept {
    return m_points[index];
};