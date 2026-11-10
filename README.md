# Mars Survival Outpost

A deterministic survival simulation with one astronaut per outpost. Complete ten sols while equipment replenishes supplies and an autonomous rover surveys terrain.

## Run the demonstration

From this `TheMartian` folder, run:

```powershell
python main.py
```

The demonstration prints initial and daily status reports, breaks the rover before sol 2, repairs it before sol 3, and recharges it before sol 6. It finishes with a keyword search of failed equipment operations and a separate water-shortage example.

Expected main-scenario results:

- Status: `SUCCEEDED` after 10 sols.
- Remaining supplies: 2 food, 0 water, 9 oxygen.
- Rover distance: 12 km.
- Logged equipment failures: rover breakdown on sol 2 and empty battery on sols 5 and 9.

The shortage example has food and oxygen but no water. It returns `FAILED` with zero completed sols and leaves both available supplies unchanged.

## Classes

| Class | Responsibility |
|---|---|
| ResourceStore | Validate and control the food, water and oxygen dictionary. |
| Astronaut | Request its daily bundle of one food, one water and one oxygen. |
| Equipment | Share operational state and the public operation that delegates to protected subclass work. |
| OxygenGenerator | Spend one water to produce two oxygen. |
| WaterExtractor | Produce three water per successful operation. |
| Greenhouse | Spend one water per growing sol; harvest three food every three successful growing sols. |
| Rover | Spend one battery unit to explore two kilometres, with a capacity of three units. |
| MissionLog | Store messages in order and return keyword-filtered copies. |
| MarsOutpost | Own the resource store and log, coordinate the equipment list, and track survival progress. |

## Daily rules

The astronaut requests the entire daily bundle first. A shortage ends the mission without partial consumption, equipment work or an increment to completed sols. A successful day increments the count; reaching the target ends the mission immediately. Otherwise, each equipment item operates once in list order.

Equipment failure does not undo a completed sol. It may reduce the supplies available for the next one. Greenhouse progress pauses during a shortage or breakdown. Rover recharging restores its charge but does not repair it. Repair, breakdown and recharge are manual demonstration actions between sols.

Use `add_supplies()` and `add_equipment()` before starting. Both setup operations lock once a sol has completed or the mission ends. Equipment instances should be assigned to only one outpost; duplicate checks apply within each outpost's equipment list.

MarsOutpost uses the taught `property()` function for read-only `sols_completed`, `target_sols` and `status`. An invalid target retains the default of ten sols. Supplying something other than an Astronaut makes the first attempted sol fail safely.

## Verification and remaining work

On 10 November 2026, 65 one-off review checks passed for the added classes and their interactions, including greenhouse pause/resume, rover battery limits, log search and copy protection, setup controls, operation priority, terminal mission states and the full ten-sol resource balance. The actual `main.py` demonstration also completed successfully.

These review checks are not a persistent pytest suite or coverage report. The final portfolio's Topic 9 tests/fixtures/coverage, Topic 10 exception-handling work, earlier classes' documentation/formatting cleanup, and genuine workshop-review records remain to be completed.
