#include <SFML/Graphics.hpp>

int main() {
    sf::RenderWindow window(sf::VideoMode(800, 600), "Simple Paint Program");
    sf::CircleShape brush(5.f); // Simple brush represented as a circle
    brush.setFillColor(sf::Color::Red);

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();

            if (event.type == sf::Event::MouseButtonPressed) {
                if (event.mouseButton.button == sf::Mouse::Left) {
                    brush.setPosition(static_cast<float>(event.mouseButton.x), static_cast<float>(event.mouseButton.y));
                    window.draw(brush);
                }
            }
        }

        window.display();
    }

    return 0;
}
