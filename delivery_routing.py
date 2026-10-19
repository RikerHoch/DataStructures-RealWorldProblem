from collections import deque
from dataclasses import dataclass
from heapq import heappush, heappop
from math import hypot
from typing import List, Tuple, Dict, Optional


@dataclass
class SearchResult:
    path: List[str]
    distance_km: float
    nodes_expanded: int


class DeliveryNetwork:

    def __init__(self):
        self.coordinates: Dict[str, Tuple[float, float]] = {
            "Warehouse": (0, 0),
            "North Hub": (2, 4),
            "West Junction": (3, 1),
            "Central Hub": (5, 3),
            "Riverside": (6, 0),
            "East Junction": (8, 3),
            "Hillcrest": (9, 6),
            "South Depot": (4, -3),
            "Customer": (11, 1),
        }
        self.graph: Dict[str, Dict[str, float]] = {
            node: {} for node in self.coordinates
        }
        self._add_road("Warehouse", "North Hub", 5.0)
        self._add_road("Warehouse", "West Junction", 3.5)
        self._add_road("Warehouse", "South Depot", 5.0)
        self._add_road("North Hub", "West Junction", 4.0)
        self._add_road("North Hub", "Central Hub", 4.0)
        self._add_road("North Hub", "Hillcrest", 8.0)
        self._add_road("West Junction", "Central Hub", 3.0)
        self._add_road("West Junction", "South Depot", 4.0)
        self._add_road("Central Hub", "Riverside", 4.0)
        self._add_road("Central Hub", "East Junction", 3.5)
        self._add_road("Central Hub", "Hillcrest", 4.5)
        self._add_road("Riverside", "East Junction", 4.0)
        self._add_road("Riverside", "Customer", 6.0)
        self._add_road("East Junction", "Customer", 3.5)
        self._add_road("East Junction", "Hillcrest", 3.0)
        self._add_road("South Depot", "RiverSide", 7.0)


def _add_road(self, a: str, b: str, km: float) -> None:
    self.graph[a][b] = km
    self.graph[b][a] = km


def heuristic(self, node: str, goal: str) -> float:
    x1, y1 = self.coordinates[node]
    x2, y2 = self.coordinates[goal]
    return 0.5 * hypot(x2 - x1, y2 - y1)


def path_distance(self, path: List[str]) -> float:
    return sum(self.graph[a][b] for a, b in zip(path, path[1:]))


class BreadthFirstSearch:

    @staticmethod
    def search(
        network: DeliveryNetwork, start: str, goal: str
    ) -> Optional[SearchResult]:
        queue = deque([start])
        parent = {start: None}
        expanded = 0

        while queue:
            current = queue.popleft()
            expanded += 1
            if current == goal:
                break
            for neighbor in network.graph[current]:
                if neighbor not in parent:
                    parent[neighbor] = current
                    queue.append(neighbor)

        if goal not in parent:
            return None
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
        return SearchResult(path, network.path_distance(path), expanded)


class AStarSearch:

    @staticmethod
    def search(
        network: DeliveryNetwork, start: str, goal: str
    ) -> Optional[SearchResult]:
        frontier = []
        heappush(frontier, (network.heuristic(start, goal), 0.0, start))
        came_from = {start: None}
        best_cost = {start: 0.0}
        expanded = 0

        while frontier:
            _, cost_so_far, current = heappop(frontier)
            if cost_so_far != best_cost.get(current):
                continue

            expanded += 1
            if current == goal:
                break

            for neighbor, road_cost in network.graph[current].items():
                new_cost = cost_so_far + road_cost
                if new_cost < best_cost.get(neighbor, float("inf")):
                    best_cost[neighbor] = new_cost
                    came_from[neighbor] = current
                    priority = new_cost + network.heuristic(neighbor, goal)
                    heappush(frontier, (priority, new_cost, neighbor))

        if goal not in came_from:
            return None
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = came_from[node]
        path.reverse()
        return SearchResult(path, network.path_distance(path), expanded)


class Observer:

    def update(self, event: str, message: str) -> None:
        raise NotImplementedError


class Driver(Observer):

    def __init__(self, name: str):
        self.name = name

    def update(self, event: str, message: str) -> None:
        if event == "route_recalculated":
            print(f"Driver {self.name} received event '{event}': {message}")


class Customer(Observer):

    def __init__(self, name: str):
        self.name = name

    def update(self, event: str, message: str) -> None:
        if event == "delivery_completed":
            print(f"[Customer Notification] {self.name}: {message}")


class DeliverySystem:

    def __init__(self, network: DeliveryNetwork):
        self.network = network
        self.observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def notify(self, event: str, message: str) -> None:
        for observer in self.observers:
            observer.update(event, message)

    def recalculate_route(self, start: str, goal: str) -> Optional[SearchResult]:
        result = AStarSearch.search(self.network, start, goal)
        if result:
            route = " -> ".join(result.path)
            self.notify(
                "route_recalculated",
                f"New route: {route} ({result.distance_km:.1f} km)",
            )
        return result


def display_result(label: str, result: Optional[SearchResult]) -> None:
    if result is None:
        print(f"{label}: No route found.")
        return
    print(f"{label} path: {' -> '.join(result.path)}")
    print(f"{label} distance: {result.distance_km:.1f} km")
    print(f"{label} nodes expanded: {result.nodes_expanded}")
    print()

def main() -> None:
    network = DeliveryNetwork()
    start, goal = "Warehouse", "Customer"

    bfs_result = BreadthFirstSearch.search(network, start, goal)
    astar_result = AStarSearch.search(network, start, goal)

    print("=== Delivery Routing Comparison ===")
    display_result("BFS", bfs_result)
    display_result("A*", astar_result)

    if bfs_result and astar_result:
        print("Note: BFS minimized road connections, not total kilometers")
        if bfs_result.nodes_expanded:
            reduction = (
                (bfs_result.nodes_expanded - astar_result.nodes_expanded)
                / bfs_result.nodes_expanded
            ) * 100
            print(f"Node-expansion change (BFS baseline): {reduction:.1f}%")
            print("A negative value indicates A* expanded more nodes in this test.")
        print()

        driver = Driver("Alice")
        customer = Customer("Bob")
        system = DeliverySystem(network)
        system.subscribe(driver)
        system.subscribe(customer)

        print("=== Observer Pattern Demonstration ===")
        system.recalculate_route(start, goal)
        system.complete_delivery(customer.name)


if __name__ == "__main__":
    main()
