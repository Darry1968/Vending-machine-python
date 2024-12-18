# Vending Machine Using python and RaspberryPI

This project aims to create a milk vending machine using Raspberry Pi as the server, which interacts with a mobile application to receive input and dispense milk accordingly. The Raspberry Pi serves as the central control unit, managing the vending process based on user requests received through the mobile app.

## Features

- **Interactive User Interface**: A simple and intuitive UI for users to select and purchase items.
- **Real-Time Inventory Management**: Tracks stock levels and updates them after each purchase.
- **Raspberry Pi Integration**: Optimized for running on Raspberry Pi hardware.

## Installation

Follow these steps to set up the Vending Machine project on your Raspberry Pi:

1. Clone the repository:
   ```bash
   git clone https://github.com/Darry1968/Vending-machine-python.git
   cd Vending-machine-python
   ```

2. Install required dependencies:
   ```bash
   pip install pybluez
   ```

3. Ensure your Raspberry Pi is configured correctly with all hardware connections set up.

4. Run the main file:
   ```bash
   python Server.py
   ```

## Usage

1. Start the server by running `Server.py` on the Raspberry Pi.
2. Interact with the vending machine through the provided interface.
3. Select items and confirm purchases.
4. The system will update the inventory and process the selection.

## Requirements

- **Python 3.8+**
- Raspberry Pi (any model with GPIO support)
- Required Python libraries:
  - `pybluez`
  - `RPi.GPIO`

## Hardware Setup

Ensure the following hardware is correctly connected to your Raspberry Pi:

- GPIO pins for buttons and display.
- Actuators/motors to dispense items.
- Power supply and additional peripherals as required.

## Project Structure

```plaintext
Vending-machine-python/
├── Server.py            # Main script to run the vending machine
```

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your branch.
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For queries or suggestions, reach out to:
- **Name**: Darshan Soni
- **Email**: [sonidarshan200@gmail.com](mailto:sonidarshan200@gmail.com)
- **GitHub**: [Darry1968](https://github.com/Darry1968)

---

_Your feedback and suggestions are highly appreciated!_
