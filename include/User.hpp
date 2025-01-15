#ifndef USER_HPP
#define USER_HPP

#include <iostream>

#include "GPSCoords.hpp"
#include "Circle.hpp"

class User {
    GPSCoords m_pos;

public:
    // Constructors
    User() = delete;
    User(GPSCoords pos);

    // Member functions
    void refresh_position(GPSCoords pos) noexcept;
    Circle get_circle() const noexcept;

    // Static
    static constexpr int DEFAULT_RADIUS = 2;
};

#endif // !USER_HPP