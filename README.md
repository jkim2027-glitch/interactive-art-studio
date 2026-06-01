# Interactive Art Studio

An interactive graphics application where users can create digital art by clicking on different colored areas of a canvas.

## Overview

This project is a creative application built with Python and CMU Graphics that allows users to explore a dynamic, artistic canvas. The application features an animated night sky with twinkling stars, an interactive house structure, and multiple human figures. Users can input custom messages that appear and fade away, creating a dynamic and engaging artistic experience that combines visual effects with user interaction.

## Features

- 🎨 **Color-based Interactive Regions**: Click on different colored circles to activate various visual elements
- ✨ **Animated Star Effects**: Star burst animations and twinkling stars that respond to user interaction
- 🏠 **Interactive Scene Elements**: House, windows, figures, and lights that toggle on/off
- 🎯 **Collision Detection**: Precise mouse event handling with visual feedback
- 🌙 **Dynamic Sky Scenes**: Day/night transitions with gradient effects
- 📝 **Real-time Feedback**: Visual responses to all user interactions

## Technologies Used

- **Python 3**: Core programming language
- **CMU Graphics**: Graphics library for visualization
- **Sound Effects**: Integrated audio feedback

## How to Run

1. Make sure you have Python installed
2. Install CMU Graphics:
   ```bash
   pip install cmu-graphics
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## How to Play

### Color Palette (Top of Screen)
Click on the colored circles to interact with the scene:

- **Red**: Create a house
- **Orange/Dark Orange**: Toggle house window
- **Yellow**: Toggle window light
- **Green/Dark Green**: Add grass/create gradient grass
- **Blue/Midnight Blue/Navy**: Change sky colors
- **Purple/Indigo**: Show different people
- **White**: Create star burst effects
- **Khaki**: Add khaki overlay

### Mouse Interaction
- **Move Mouse**: Brush follows your cursor (when not in the color palette)
- **Click**: Trigger effects and sounds
- **Hold**: Create burst effects when not hovering over interactive elements

## Project Structure

```
interactive-art-studio/
├── main.py          # Main application code
├── README.md        # This file
└── requirements.txt # Project dependencies
```

## Key Challenges & Learning

This project taught me several important lessons:

1. **State Management**: Managing multiple interactive elements and their states efficiently
2. **Collision Detection**: Implementing precise hit detection for smooth user interaction
3. **Animation Systems**: Creating smooth animations by manipulating object properties over time
4. **User Interface Design**: Building intuitive interfaces through visual feedback
5. **Code Organization**: Structuring complex graphics code into logical groups

## Future Improvements

- [ ] Add more interactive elements
- [ ] Implement save/load functionality
- [ ] Add more sound effects
- [ ] Create presets or themes
- [ ] Add animation sequences

## Author

Yeon - 2026

## License

This project is part of my portfolio and is available for educational purposes.
