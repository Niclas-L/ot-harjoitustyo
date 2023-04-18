# Ohjelmistotekniikka, harjoitustyö
# Pygame 2048

Implementation of the [2048](https://en.wikipedia.org/wiki/2048_(video_game))-game in python using pygame.
Currently the game is played using the arrow keys or the wasd keys. The escape key can be used to reset the game (no confirmation so beware).

## Documentation

- [Vaatimusmäärittely](https://github.com/Niclas-L/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/Niclas-L/ot-harjoitustyo/blob/master/documentation/tuntikirjanpito.md)
- [Arkitehtuurikuvaus](https://github.com/Niclas-L/ot-harjoitustyo/blob/master/documentation/arkitehtuuri.md)
- [Changelog](https://github.com/Niclas-L/ot-harjoitustyo/blob/master/documentation/changelog.md)

## Installing
1. Install dependepncies by running the following command
```
poetry install
```
2. Start the application using the following command:
```
poetry run invoke start
```

## Command line functionality
### Starting the application
The following command runs the application:
```
poetry run invoke start
```
### Testing
The following command runs the implemented unittests:
```
poetry run invoke test
```
### Coverage report
The following command generates a coverage report of the unittests:
```
poetry run invoke coverage-report
```
### Pylint
Style specifications in .pylintrc can be confirmed using the following command:
```
poetry run invoke lint
```
