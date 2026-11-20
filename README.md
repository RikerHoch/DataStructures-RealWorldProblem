# 🚚 Delivery Routing System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-brightgreen)
![Algorithms](https://img.shields.io/badge/Algorithms-BFS%20%7C%20A*-blue)
![Design Pattern](https://img.shields.io/badge/Design%20Pattern-Observer-purple)

A Python-based delivery routing simulation that uses a **weighted, undirected graph** to compare **Breadth-First Search (BFS)** and **A* Search**. It also demonstrates the **Observer design pattern** by notifying drivers when routes are recalculated and customers when deliveries are completed.

> **Coursework project:** Developed to demonstrate graph data structures, search algorithms, object-oriented programming, and event-driven notifications.

## 📌 Project Overview

The simulation models a delivery company that needs to find a route between a warehouse and a customer.

Each location is represented as a node, each road as an edge, and each road has an associated distance in kilometres.

The program compares two search algorithms:

- **BFS:** Finds the route with the fewest road connections.
- **A* Search:** Uses road distances and a heuristic to find a shorter-distance route.

The project also includes a notification system using the Observer Pattern.

## ✨ Key Features

- 🗺️ **Weighted graph:** Nine delivery locations connected by 16 two-way roads.
- 🔎 **Breadth-First Search:** Uses a queue to explore routes.
- ⭐ **A* Search:** Uses a priority queue and distance heuristic.
- 📊 **Performance comparison:** Displays route distances and expanded nodes.
- 🔔 **Observer Pattern:** Notifies drivers and customers of delivery events.
- 🧩 **Object-oriented design:** Uses classes, inheritance, and modular functions.
- 🐍 **Standard Python libraries:** No external dependencies required.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Dictionaries | Graph representation |
| `collections.deque` | BFS queue |
| `heapq` | A* priority queue |
| `math.hypot` | Distance heuristic |
| `dataclasses` | Search result storage |
| Observer Pattern | Delivery notifications |

## 📂 Project Structure

```text
Delivery-Routing-System/
├── delivery_routing.py
└── README.md
```



---

<p align="center">
  <strong>🧪 Clean data · 🏗️ Maintainable design · 📊 Useful reports</strong><br>
  <sub>Developed for BACT 7603 Data Structures — Assessment 2, 2026.</sub>
</p>
