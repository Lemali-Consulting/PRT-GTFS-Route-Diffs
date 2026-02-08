# PRT-GTFS-Route-Diffs

Compares Pittsburgh Regional Transit GTFS schedule feeds across time periods to identify changes in arrival times by route and headsign direction. Currently compares the October 2025 and January 2026 feeds.

## Project Structure

```
PRT-GTFS-Route-Diffs/
├── src/
│   └── main.py                       # Main analysis script
├── zips/                             # Compressed GTFS feed archives
│   ├── GTFS_August_14_2025.zip
│   ├── GTFS_October_16_2025.zip
│   └── GTFS_January_26_2026.zip
├── August_14_2025/                   # Extracted GTFS data
├── October_16_2025/                  # Extracted GTFS data
└── January_26_2026/                  # Extracted GTFS data
```

Each extracted directory contains a standard GTFS feed (~100 routes, ~6,500 stops, ~850K stop time records):

| File | Description |
|------|-------------|
| `stop_times.txt` | Arrival/departure times at each stop (primary input) |
| `trips.txt` | Trip definitions linking routes to stop sequences |
| `routes.txt` | Route names and metadata |
| `stops.txt` | Stop locations and names |
| `shapes.txt` | Geographic route paths |
| `calendar.txt` / `calendar_dates.txt` | Service schedules and exceptions |

## Prerequisites

- Python 3.x (no external dependencies; uses only the standard library)

## Usage

```bash
python src/main.py
```

The script reads `stop_times.txt` from both the October 2025 and January 2026 feeds, groups arrival times by route headsign direction, and prints the time differences where schedules changed between the two feeds.

## How It Works

1. Parses `stop_times.txt` from the October 2025 feed and organizes arrival times by trip headsign
2. Parses `stop_times.txt` from the January 2026 feed and adds new arrival times to the same structure
3. For each headsign direction, sorts and compares arrival times between the two feeds
4. Outputs the route name and time differences where changes were detected

## Limitations

- Compares sorted arrival times only; does not align by specific stop or trip sequence
- Paths to the two feeds being compared are hardcoded in `main.py`
- August 2025 data is present but not currently used in the comparison
- Output is printed to stdout with no file export option
