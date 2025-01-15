#include "GPSCoords.hpp"

GPSCoords::GPSCoords() :
    m_latitude(0.0), m_longitude(0.0) {}

GPSCoords::GPSCoords(double latitude, double longitude) {
    if (latitude < -90.0 || latitude > 90.0) {
        throw std::invalid_argument("Latitude must be between -90.0 and 90.0");
    }
    if (longitude < -180.0 || longitude > 180.0) {
        throw std::invalid_argument("Longitude must be between -180.0 and 180.0");
    }

    m_latitude = latitude;
    m_longitude = longitude;
}

/**
 * @brief Calculates the euclidian distance to another point (GPSCoords)
 */
double GPSCoords::distance(GPSCoords p) const {
    return std::sqrt(std::pow((m_latitude - p.m_latitude), 2) + std::pow((m_longitude - p.m_longitude), 2));
}

std::ostream& operator<<(std::ostream& os, const GPSCoords& coords) {
    os << "GPSCoords(lat=" << coords.m_latitude << ", long=" << coords.m_longitude << ")";
    return os;
}
