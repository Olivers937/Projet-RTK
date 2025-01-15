#include "Circle.hpp"

Circle::Circle(GPSCoords center, double radius)
    : m_center(center), m_radius(radius) {};

/**
 * @brief Check if this circle contains a point
 * 
 * @return True if Yes
 */
bool Circle::contains(GPSCoords point) const noexcept {
    double x1 = m_center.longitude();
    double y1 = m_center.latitude();
    
    double x2 = point.longitude();
    double y2 = point.latitude();

    double distance = std::hypot(x2 - x1, y2 - y1);;

    return distance < m_radius;
}