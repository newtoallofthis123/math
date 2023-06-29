# Days Tracker

This is the folder in which all the days will be stored. Each day will have a file named `day-<day-number>.md` and will be stored in the `days` folder.

The `info.json` file contains the information about the tracker. It contains the following information:

```json
{
    "days": "number of days",
}
```

The `days` folder is mostly used by the `/scripts/track.py` script to generate the day files and the `info.json` file.

Regardless, the `days` folder is the folder where all the day files are stored.
