#ifndef CIRCLE_HPP
#define CIRCLE_HPP

#include "GPSCoords.hpp"
#include "cmath"

class Circle {
    GPSCoords m_center;
    double m_radius;

public:
    // Constructors
    Circle(GPSCoords center, double radius);

    // Member functions
    bool contains(GPSCoords point) const noexcept;
};

#endif // !CIRCLE_HPP