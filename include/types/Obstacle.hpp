#include <string>

struct ObstacleData {
    std::string sensor_id;
    std::string priority;
    double distance;
    double angle;
    double confidence;
};