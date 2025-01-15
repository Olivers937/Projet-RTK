#include "User.hpp"

User::User(GPSCoords pos) {
    m_pos = pos;
}

/**
 * @brief Refresh the actual position of the user
*/
void User::refresh_position(GPSCoords pos) noexcept {
    m_pos = pos;
}

/**
 * @brief Constructs and returns the DEFAULT_RADIUS-radius circle containing the user
 */
Circle User::get_circle() const noexcept {
    return Circle(m_pos, DEFAULT_RADIUS);
}
