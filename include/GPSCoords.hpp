#ifndef GPSCOORDS_HPP
#define GPSCOORDS_HPP

#include <iostream>
#include <cmath>
#include <vector>
#include <stdexcept>

class GPSCoords {
    double m_latitude;
    double m_longitude;

public:
    // Constructors
    GPSCoords();
    GPSCoords(double latitude, double longitude);

    // Accessors
    double latitude() const noexcept { return m_latitude; };
    double longitude() const noexcept { return m_longitude; };

    // Member functions
    double GPSCoords::distance(GPSCoords p) const;

    // Operators
    friend std::ostream& operator<<(std::ostream& os, const GPSCoords& coordinates);
};

#endif // !GPSCOORDS_HPP