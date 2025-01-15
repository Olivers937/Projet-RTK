#ifndef PATH_HPP
#define PATH_HPP

#include "GPSCoords.hpp"

class Path {
    int m_actual_index;
    std::vector<GPSCoords> m_points;

public:
    // Constructors
    Path(GPSCoords start_point, GPSCoords end_point);

    // Accessors, Getters
    int actual_index() const noexcept { return m_actual_index; };
    std::vector<GPSCoords> points() const noexcept { return m_points; };
    void points(std::vector<GPSCoords> points) { m_points = points; };
    
    // Member functions
    GPSCoords get_point(int index) const noexcept;

    // Static functions
    static std::vector<GPSCoords> construct_path(GPSCoords start_point, GPSCoords end_point);
};

#endif // !PATH_HPP