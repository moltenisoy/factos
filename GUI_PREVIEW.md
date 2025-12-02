# GUI Preview

The application features a modern card-based interface inspired by the reference design.

## Layout

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│   Select Optimization Options                                │
│                                                               │
│   ┌───────────────────────────────────────────────────┐     │
│   │ ✓ Apply All Optimizations                         │     │
│   └───────────────────────────────────────────────────┘     │
│                                                               │
│   ┌───────────────────────────────────────────────────┐     │
│   │ Network Optimizations                    [○──]    │     │
│   │ Optimize TCP/IP settings, DNS cache, and          │     │
│   │ network adapter configurations                    │     │
│   └───────────────────────────────────────────────────┘     │
│                                                               │
│   ┌───────────────────────────────────────────────────┐     │
│   │ Graphics & GPU                           [──○]    │     │
│   │ Optimize GPU driver settings, disable GPU         │     │
│   │ throttling, improve frame latency                 │     │
│   └───────────────────────────────────────────────────┘     │
│                                                               │
│   ┌───────────────────────────────────────────────────┐     │
│   │ Power Management                         [──○]    │     │
│   │ Maximize performance, disable CPU throttling,     │     │
│   │ optimize power settings                           │     │
│   └───────────────────────────────────────────────────┘     │
│                                                               │
│   ┌───────────────────────────────────────────────────┐     │
│   │ Privacy & Telemetry                      [──○]    │     │
│   │ Disable telemetry, tracking, and data             │     │
│   │ collection services                               │     │
│   └───────────────────────────────────────────────────┘     │
│                                                               │
│   ┌───────────────────────────────────────────────────┐     │
│   │ System Services                          [──○]    │     │
│   │ Disable unnecessary Windows services and          │     │
│   │ scheduled tasks                                   │     │
│   └───────────────────────────────────────────────────┘     │
│                                                               │
│   ┌───────────────────────────────────────────────────┐     │
│   │ Storage & File System                    [──○]    │     │
│   │ Optimize disk performance, disable indexing       │     │
│   │ and compression                                   │     │
│   └───────────────────────────────────────────────────┘     │
│                                                               │
│   ┌───────────────────────────────────────────────────┐     │
│   │ Windows Updates                          [──○]    │     │
│   │ Disable automatic updates and related             │     │
│   │ services                                          │     │
│   └───────────────────────────────────────────────────┘     │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## Color Scheme

- Background: Dark blue-gray (#1c2833)
- Cards: Medium blue-gray (#2d3e50)
- Text: Light gray/white (#ecf0f1)
- Description: Light gray (#95a5a6)
- Toggle OFF: Red (#c0392b)
- Toggle ON: Green (#27ae60)
- Apply All Button: Blue (#2980b9)

## Toggle Switch States

- **Red Switch (Left)**: Optimization is disabled
- **Green Switch (Right)**: Optimization is enabled

## Features

- Wide card-based design matching the reference image
- Toggle switches change color from red to green when enabled
- No popups or notifications - only visual feedback via switch color
- Automatic backup before applying optimizations
- Automatic restore when disabling optimizations
- "Apply All" button at the top to enable all optimizations at once
- Smooth, modern interface with proper spacing
