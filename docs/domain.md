# EU Electricity Market — Domain Notes

> Personal study notes consolidating my understanding of the European
> electricity system, ENTSO-E, and the wholesale power markets that this
> project's data comes from. Written for future-me. May contain mistakes;
> updated as I learn more.

**Last updated**: 2026-05-23
**Status**: Living document

---

## How to use this doc

This is a notebook, not an encyclopaedia. When something I wrote here
turns out to be wrong, I correct it and note the change in the journal.

**Disclaimer**: AI was used as a tool to help me write in way that is easy for the reader to follow throgh by rephrasing it or add points I have learned from by using it as a learningg tool as well, so do your own due diligence after knowing this fact.

---

## 1. The big picture

- What is ENTSO-E, in one paragraph? (Hint: who founded it, when, why does
  it exist, who does it represent.)
- What problem does it solve that a single national TSO couldn't solve
  alone?
- What's the *physical* European grid vs the *organisational* ENTSO-E?
  Are they the same thing? (No — explain the difference.)

Founded by transmission system operators (TSOs) in 2009 and a legal basis — EU Regulation (EC) 714/2009, The European Network of Transmission System Operators for Electricity(ENTSO-E) is an association representing 40 electricity transmission system operators(TSOs) from 36 countries across Europe unifying together to balance the supply/demand of electricity and ensure availability and security of the whole electricity infrastructure by coordinating between them (publishes standards, runs the Transparency Platform, develops the Ten-Year Network Development Plan, harmonises rules via network codes, calculates cross-border capacity). So, ENTSO-E doesnt do the balancing, it just coordinates TSOs that are responsible to do that.

TSOs, although powerful, are not very strong to solve all problems single handedly. So they need better coordinationa and synchronization with all other TSOs in the region and EU, to solve that, they need to tell their peers about where their parts are and how they doing business in terms of load on their grid, so under CGMES standard, they share their(IGM) and together they form a CGM and now ENTSO-E can give them ability to do cross-border capacity calculation (impossible without merging IGMs), benefit from a single EU electricity market (impossible without harmonised rules).

Physical European grid is a physical infrastructure of cables, transformers, and power plants, while ENTSO-E organizationaly is a Brussels-based association of 40 companies. Comparing them is like saying "a road and the transport ministry are the same."

---

## 2. Synchronous areas — the physical map

- What is a "synchronous area"? Why can't power just flow freely between
  any two countries in Europe?
- List the five synchronous areas in Europe (you saw them earlier).
- Which area is Finland in? Which is Germany in? What's the implication
  for power flowing between them?
- What's an HVDC interconnector, and why does it matter when crossing
  synchronous-area boundaries?
- What happened in February 2025 with the Baltic states? Why is
  that historically significant?

A synchronous area is a region in which all the generators rotate in lockstep at the same electrical frequency. Inside it, frequency is one number everywhere (50.0 Hz nominal). Between two synchronous areas, frequency drifts independently, so you can't connect them with regular AC cables — only HVDC.

Synchronous areas in Europe are: Continental Europe(like Germany), Nordic(like Finland), Great Britain, Ireland and Northern Ireland (often called the Ireland synchronous area), Baltic.

DE-LU →(Kontek HVDC)→ DK-East →(Storebælt)→ DK-West→(NordLink HVDC)→ NO2 →(synchronous AC)→ NO1 → SE3 →(synchronous AC)→ SE2 → SE1 →(Fenno-Skan HVDC)→ FI

Those countryside towers are almost always HVAC (High Voltage Alternating Current), not HVDC. HVDC is a specific technology used for:
Connecting two non-synchronous areas (you can't link Nordic and Continental Europe with AC — frequencies drift)
Very long-distance transmission (~700 km+) where AC losses are unacceptable
Subsea or underground cables (AC capacitance kills long subsea AC lines)

HVDC requires converter stations at each end (AC→DC, DC→AC). Examples: Fenno-Skan (Finland-Sweden, undersea), Estlink 1+2 (Estonia-Finland, subsea), NordLink (Norway-Germany, subsea). These don't look like countryside towers — they're subsea cables with big buildings at each end.

Estonia, Latvia, Lithuania disconnected from the post-Soviet BRELL grid (Belarus, Russia, Estonia, Latvia, Lithuania) and synchronised with Continental Europe via Poland. This was a planned, successful decoupling — not a blackout.
Historical significance: ends 60 years of dependence on the Russian grid; geopolitical milestone tied to the war in Ukraine; engineering milestone because you don't normally re-sync 3 countries to a new area without disruption.

---

## 3. Key actors and their roles

- **TSO** (Transmission System Operator): For Finland it is Fingrid and many countries can have at least one of them as these are the main power coordinators within a country and all other electricity companies or big consumers should interact with them. they specifically operate high-voltage transmission (typically 110 kV and above in Finland; 220/380 kV in continental EU).
- **DSO** (Distribution System Operator): In most EU markets (including Finland), the ordinary person signs an electricity supply contract with a retailer (Helen, Lumme, Oomi, Väre, etc.), not directly with the DSO. The DSO bills the network/distribution fee separately. Two contracts, two parties.
- **NEMO** (Nominated Electricity Market Operator): The entity that runs the day-ahead and intraday market coupling for a bidding zone (the actual price-setting mechanism). In the Nordics it's Nord Pool. In continental Europe, EPEX SPOT is dominant.
- **BRP** (Balance Responsible Party): A BRP is financially responsible for matching their schedule to their actual delivery/consumption in real time. If they're off-schedule, they pay imbalance charges. Every market participant has to either be a BRP themselves or be represented by one. So BRP is broader than "bidder."
- **BSP** (Balancing Service Provider): An entity in the electricity market that helps maintain the balance between electricity supply and demand by providing various balancing services, such as Frequency Containment Reserve (FCR) and Automatic Frequency Restoration Reserve (aFRR). These services are crucial for ensuring the stability of the power grid.
- **Generator** : An electromechanical device that converts mechanical energy to electrical energy for use in an external circuit. Small generators (a single wind farm, a rooftop solar plant) often don't have their own BRP status — they sell their output to an aggregator or a utility who acts as their BRP.
- **Retailer / supplier** : The company you the customer pays your electricity bill to. They buy in the wholesale market (or from a generator) and sell to end consumers. In Finland, Helen, Lumme Energia, Oomi, Väre, Fortum Markets are examples.
- **Aggregator** : Pools many small flexible resources (batteries, EV chargers, factory loads) into one "virtual" resource big enough to participate in the wholesale or balancing market. Sympower and Ingrid Capacity in your region.
- **Power exchange** : these are closely related but not identical. A power exchange is the organisation that runs the marketplace. NEMO is a regulatory designation. Nord Pool is both: it's a power exchange, and it's the designated NEMO for the Nordics. EPEX SPOT is both.
- **Regulator** : ACER sets EU-wide rules and arbitrates between national regulators. Energiavirasto is the Finnish national regulator that sets DSO/TSO allowed returns, approves tariffs, monitors market behaviour. Sister regulators in other EU countries: Bundesnetzagentur (Germany), CRE (France), Ofgem (UK — post-Brexit but still relevant), CNMC (Spain).

---

## 4. The wholesale markets

There are three main timeframes. For each, answer:
- When does it trade? (the clock-times matter)
- What's the granularity (hour, 15 min)?
- What kind of participants dominate?
- What's the price-setting mechanism?

### Day-ahead market (DA)

- **When**: bids submitted through the morning; gate closes at **12:00 CET**.
  The market is for delivery the **next day** (D+1) — every hour of tomorrow.
- **Granularity**: one price per **bidding zone**, per **hour** (the EU is
  moving toward a 15-minute MTU — Market Time Unit).
- **Who participates**: nearly everyone — generators, retailers, large
  industrial consumers, traders, battery operators — each acting through a
  **BRP** (Balance Responsible Party).
- **How the price is set**: not bilateral. All bids go into a **pool**. At
  12:00 the **Euphemia** algorithm runs **market coupling** across all
  coupled zones at once, respecting interconnector capacities, and produces
  **one clearing price per zone per hour**. Results publish ~12:42 CET,
  final ~13:00 CET.
- **If you clear but reality differs**: once cleared, you're committed. A
  seller who under-delivers, or a buyer who consumes more/less than bought,
  is **in imbalance** and pays **imbalance charges** (settled days later).
  Nobody "rejects" a delivery — the pool already matched everything;
  mismatches are purely financial.

### Intraday market (ID)

- **When**: opens when day-ahead results are known; trades **continuously**
  until close to delivery (commonly ~5–60 minutes before the hour).
- **Granularity**: hourly plus shorter 15- and 30-minute products.
- **Who participates**: anyone needing to **adjust their position** after
  day-ahead — a wind farm whose forecast changed, a battery chasing a price
  move, a trader working a spread.
- **How the price is set**: **continuous trading**, like a stock-exchange
  order book — live buy/sell offers, trade against them, no single clearing
  price. European ID markets are linked via **SIDC** (Single Intraday
  Coupling).
- **Why it exists**: wind, solar, and demand forecasts get more accurate as
  delivery approaches. The ID market lets participants correct the position
  they locked in at day-ahead.

### Balancing market (BAL)

#### Part 1: the physical fix (reserve activation).

The TSO (Fingrid) watches frequency continuously. Below 50 Hz = shortage; above = surplus. To fix it, the TSO activates reserves that BSPs (Balancing Service Providers) pre-sold:

* FCR auto-responds in seconds — arrests the deviation.

* aFRR auto-responds in seconds-to-minutes — restores frequency to 50.

* mFRR is manually ordered within minutes for bigger events.

These are real resources: a gas plant ramps up, a battery discharges, a demand-response aggregator curtails factory load. Shortage → activate upward reserves (generate more / consume less). Surplus → activate downward reserves.

#### Part 2: the financial fix (imbalance settlement).

##### Concrete money flow
6pm hour. A gas plant scheduled for 200 MW trips at 6:15 — instant 200 MW shortage. Frequency starts dropping.

1- FCR auto-arrests the drop within seconds across the synchronous area.

2- Fingrid activates aFRR/mFRR — a battery (BSP) discharges, a hydro plant (BSP) ramps up — to cover the 200 MW.

3- Fingrid pays those BSPs for the balancing energy.

4- Days later: the gas plant's BRP is found 200 MW short. It's billed the imbalance price for that volume. That money roughly covers what Fingrid paid the BSPs.

So the flow is: the BRP who caused the problem → TSO → the BSPs who fixed it.

- **When**: **real-time**, operated separately by each TSO (Fingrid for
  Finland).
- **Why it exists**: day-ahead and intraday only *schedule* power. Reality
  always deviates — a plant trips, wind drops, demand spikes. The balancing
  market keeps the grid at exactly **50.0 Hz second by second**.
- **Who participates**: **BSPs** (Balancing Service Providers) — generators,
  batteries, and demand-response aggregators pre-qualified to sell reserve
  capacity and energy to the TSO.
- **How it works**: the TSO activates reserves as needed; the cost is
  charged back to whichever BRP caused the imbalance, via **imbalance
  settlement**.

**Plus the reserves:** what's the difference between FCR, aFRR, mFRR?
Order them from fastest activation to slowest, and write one line
each on what triggers them.

Ordered fastest to slowest:

- **FCR** (Frequency Containment Reserve) — activates within **seconds**,
  fully automatic. *Arrests* a frequency deviation — stops it getting worse.
  Shared across the whole synchronous area.
- **aFRR** (automatic Frequency Restoration Reserve) — activates within
  ~**30 seconds to 5 minutes**, automatic. *Restores* frequency back to
  50.0 Hz and frees up FCR for the next event.
- **mFRR** (manual Frequency Restoration Reserve) — activates within
  ~**5–15 minutes**, manually ordered by the TSO. Backstop for larger or
  longer-lasting deviations.

Memory hook: **FCR catches it, aFRR restores it, mFRR backs them up.**

---

## 5. A worked example — one trade end-to-end

Write your own version of the bidding scenario we walked through. Pick
either:

- A Finnish generator (e.g. Helen) selling into the FI day-ahead market
- A battery operator (e.g. Ingrid Capacity) arbitraging SE3 prices
- A German industrial consumer buying for the next-day evening peak

Walk through the clock-ticks:

1. **11:30 CET** — what does the participant do?
2. **11:55 CET** — what's happening behind the scenes at the TSOs?
3. **12:00 CET** — gate closure. What's locked in?
4. **12:42 CET** — clearing prices published. What does our actor learn?
5. **13:00 CET** — final and binding. Intraday opens.
6. **Next day, the delivery hour** — what physically happens?
7. **Days later** — how does the money flow?

Use the abbreviations as they appear. The point is you can read them
back in 6 months and still follow it.

*Scenario: Helen (a Helsinki generator + retailer) selling into the Finnish
day-ahead market. All times CET.*

- **Wednesday ~11:30** — Helen's trading desk decides to offer 50 MWh from
  a CHP plant for **hour 19:00–20:00 on Thursday**. They submit a sell offer
  to **Nord Pool** (the **NEMO** for the Nordics): "50 MWh, FI zone, hour 19,
  minimum €80/MWh."
- **~11:55** — Every TSO (Fingrid, Svenska kraftnät, Statnett, Energinet…)
  submits its **IGM**; ENTSO-E merges them into the **CGM**; cross-border
  capacities (**NTC/ATC**) for hour 19 are set.
- **12:00 — gate closure**. Bidding closes. The **Euphemia** algorithm
  starts market coupling.
- **~12:42 — clearing prices published**. Say FI clears at **€85/MWh** for
  hour 19. Helen's €80 floor is below €85, so the offer **clears**. Helen is
  now committed to inject 50 MWh during hour 19 and will receive
  50 × €85 = **€4,250**.
- **13:00 — final and binding. Intraday opens**. If Helen's plant later
  looks unable to make full output, they can buy back part of the position
  on the **intraday market** before delivery.
- **Thursday 18:00–19:00 — delivery**. Helen's plant injects the power.
  Grid frequency is held near 50.0 Hz by **FCR/aFRR** across the synchronous
  area. If Helen delivers only 45 MWh, the 5 MWh shortfall is an
  **imbalance** charged to Helen's **BRP**.
- **A few days later — settlement**. Nord Pool pays Helen; grid fees flow
  to Fingrid; any imbalance charges are billed; cross-border **congestion
  rent** is split between TSOs.

---

## 6. Cross-border power flow — contract vs physics

**Prompts:**

- When a Finnish trader "buys 100 MWh from Germany," what does that
  actually mean contractually?
- Does the electricity physically travel from Germany to Finland on a
  single line? Why or why not?
- Trace the *physical* path from DE-LU to FI on the EU grid (which
  interconnectors, which intermediate zones).
- What's the Inter-TSO Compensation (ITC) mechanism, and why does it
  exist?
- What's "congestion rent" and who gets it?

**The contract side**: when a Finnish BRP "buys 100 MWh from Germany," there
is no direct German-to-Finnish deal. All bids enter the coupled day-ahead
pool. If the FI price ends up higher than the DE-LU price, the **Euphemia**
algorithm schedules power to "flow" from DE toward FI on paper — up to the
available interconnector capacity — to push the two prices closer together.
The Finnish buyer settles at the FI clearing price, the German seller at the
DE-LU price, and the spread (the **congestion rent**) goes to the TSOs whose
interconnectors carried it.

**The physics side**: electricity can't be addressed to a destination. It
flows by physical law (Kirchhoff's laws), splitting across every available
path. Finland (Nordic synchronous area) and Germany (Continental Europe
synchronous area) are not directly AC-connected — power moves between them
only through **HVDC** links. A rough physical path:

```
DE-LU →(Kontek HVDC)→ DK-East →(Storebælt)→ DK-West
      →(NordLink HVDC)→ NO2 →(AC)→ NO1 → SE3
      →(AC)→ SE2 → SE1 →(Fenno-Skan HVDC)→ FI
```

**The reconciliation**: there is never a literal "Germany sold to Finland"
transaction. The market is one big equilibrium calculation; physical flows
and financial trades are matched by netting, and transit countries are
compensated via the **Inter-TSO Compensation (ITC)** mechanism.

**Why this matters for the project**: "scheduled commercial exchanges"
(the contract side) and "physical flows" (the physics side) are *separate
datasets* on the ENTSO-E platform, and they will not show identical numbers.
The data model must keep them distinct.

---

## 7. Grid security — the three meanings

ENTSO-E uses "security" in different senses. Define each:

- **Operational / system security** — second-by-second. What is the
  N-1 criterion? Give an example.
- **Adequacy** — over weeks/months/seasons. What's a "dunkelflaute"?
- **Security of supply** — over years. Whose problem is this?

Then: write a paragraph about either the **January 8, 2021** Continental
Europe split event or the **April 28, 2025** Iberian blackout. What
happened? Why? What did the post-incident report conclude (if you've read
it)? What does "low system inertia" mean?

"Security" here is a technical term about **system stability**, not cybersecurity.
It has three overlapping meanings:

**Operational (system) security** — second-by-second physics. The grid must
hold 50.0 Hz, keep voltages in band, keep no line overloaded, and satisfy the
**N-1 criterion**: at any moment, any single component (a generator, a line, a
transformer) can fail without cascading into a blackout. N-1 is the foundational
rule of European grid operation.

**Adequacy** — over weeks, months, seasons: is there *enough* dispatchable
capacity to meet demand plus reserves? A grid can be operationally secure right
now and still face an adequacy gap next winter. A **dunkelflaute** — a cold,
dark, windless stretch — is the classic adequacy stress test.

**Security of supply** — over years: is there enough investment in generation,
interconnection, and storage to keep the lights on long-term? This is the
political/regulatory version; it appears in EU directives and ACER reports.

**Real event — the Iberian blackout, 28 April 2025.** Spain, Portugal, and
parts of southern France lost power for several hours. The investigation
pointed to a cascading frequency event in a grid running on very high
solar/wind and therefore low **inertia** — too few spinning synchronous
machines to buffer the disturbance. It made "inertia," "grid-forming
inverters," and "synchronous condensers" everyday vocabulary across the
industry in 2025–2026. It's the reference example for why operational security
gets *harder* as renewables grow.

---

## 8. Bidding zones and EIC codes

**Prompts:**

- What is a bidding zone? Why doesn't every country = exactly one zone?
- Give an example of a country split into multiple zones (and why).
- What's an EIC code? What does the FI bidding zone code look like?
- Why does the API use these codes instead of human-readable names?

A **bidding zone** is the geographic unit electricity is priced in. Within a zone there's one price per hour; between zones, prices differ when transmission
is constrained.

Mostly one zone per country — but not always. Norway has 5 (NO1–NO5), Sweden 4
(SE1–SE4), Italy several. Germany and Luxembourg share one zone (DE-LU). Splits
usually reflect internal transmission bottlenecks: if power can't flow freely
within a country, it gets priced as separate zones.

An **EIC code** (Energy Identification Code) is a 16-character identifier for
every market object — bidding zones, participants, generating units,
interconnectors. The Finnish bidding zone is `10YFI-1--------U`.

Why codes, not names: they're unambiguous, language-neutral, machine-readable,
and stable. "Finland" is ambiguous (country? bidding zone? control area?); the
EIC code is exact. The ENTSO-E API uses them everywhere — my ingestion code
will pass EIC codes, not names.

---

## 9. The data exchange layer — IGM, CGM, CGMES

**Prompts:**

- What is an IGM? What does it contain (just wires? or also operational
  state?)
- What's the CGM, and how is it built from IGMs?
- What's CGMES, in one line?
- Why does ENTSO-E need this? (Hint: cross-border capacity calculation,
  security analysis across the whole synchronous area.)

**IGM (Individual Grid Model)** — a full snapshot of one TSO's grid: topology
(substations, lines, transformers), switching state, generator dispatch, load,
and interconnector flows. Both the physical wiring *and* the operational state.

**CGM (Common Grid Model)** — all 39+ IGMs merged into one model of the whole
interconnected system, assembled via regional coordination.

**CGMES (CGM Exchange Standard)** — the XML-based format TSOs use to exchange
these models. Built on the Common Information Model (CIM).

Why it exists: you can't calculate cross-border transmission capacity, or run
security analysis across a synchronous area, from one country's view alone.
Power flows ignore borders, so the analysis needs the merged picture. Capacity
calculation and coordinated security assessment run on the CGM.

---

## 10. The Finnish landscape — who's who

### Finland's TSO

- **Fingrid** — Finland's sole TSO. Operates the high-voltage backbone
(110 kV+), runs the Finnish balancing market. Regulated monopoly, partly
state-owned.

### Top Finnish DSOs

- **Caruna** (~720k customers, largest, infrastructure-investor owned)
- **Elenia** (~440k, central Finland)
- **Helen Sähköverkko** (Helsinki, city-owned)
- Other: ~75 smaller municipal/regional DSOs.

### Major Finnish generators

- Fortum — (largest producer, partly state-owned,
nuclear + hydro)
- Helen — (Helsinki utility, generation + retail)
- *TVO (Teollisuuden Voima) —  (operates the Olkiluoto nuclear plants)
- *Pohjolan Voima (PVO) — (industrial-owned consortium).
- Others: Wind developers: Ilmatar, Megatuuli, OX2,
Taaleri.

### BESS operators & aggregators active in Finland / Nordics

- Ingrid Capacity
- Sympower
- Forus

### Power exchange

- Nord Pool — runs the day-ahead and intraday markets for
the Nordic and Baltic regions.

### Regulator

- Energiavirasto — the Finnish national energy regulator; sets
allowed returns for DSOs and the TSO, monitors the market. EU-level
counterpart: **ACER**.

***Mankala principle (Finnish quirk)** — a corporate model where a power company
is owned by its customers (industrial firms, municipalities) and sells power to
them at cost, not for profit. TVO and PVO work this way. Unique to Finland.

---

## 11. Glossary

### Organisations & roles

- **ENTSO-E** — European Network of Transmission System Operators for
  Electricity. EU-level association of ~40 TSOs; coordinates the grid, runs the
  Transparency Platform, sets standards. Founded 2009.
- **TSO** — Transmission System Operator. Operates a country's high-voltage
  backbone. Fingrid in Finland.
- **DSO** — Distribution System Operator. Operates the local medium/low-voltage
  network — the last mile to consumers.
- **NEMO** — Nominated Electricity Market Operator. Runs day-ahead/intraday
  market coupling for bidding zones. E.g. Nord Pool, EPEX SPOT.
- **BRP** — Balance Responsible Party. Financially responsible for matching its
  schedule to actual delivery/consumption; pays imbalance charges.
- **BSP** — Balancing Service Provider. Pre-qualified to sell reserves
  (FCR/aFRR/mFRR) to the TSO.
- **ACER** — EU Agency for the Cooperation of Energy Regulators. Sets EU-wide
  rules, arbitrates between national regulators.
- **Energiavirasto** — the Finnish national energy regulator.
- **Nord Pool** — the power exchange / NEMO for the Nordic and Baltic markets.
- **EPEX SPOT** — the dominant power exchange for Continental Europe.

### Market / time concepts

- **Day-ahead market (DA)** — auction closing 12:00 CET for next-day hourly
  delivery; one clearing price per zone per hour.
- **Intraday market (ID)** — continuous trading after DA up to near real time;
  corrects positions as forecasts sharpen.
- **Balancing market (BAL)** — real-time, TSO-operated; keeps frequency at 50 Hz.
- **MTU** — Market Time Unit. The trading granularity (60 min, moving to 15 min).
- **Gate closure** — the deadline after which bids can't be submitted or changed
  for a given market.
- **Bidding zone** — geographic unit electricity is priced in.
- **Synchronous area** — region where all generators run in sync at one frequency.

### Operational / technical

- **N-1 criterion** — the grid must survive any single component failure without
  losing customers.
- **FCR** — Frequency Containment Reserve. Seconds, automatic. Arrests frequency
  deviations.
- **aFRR** — automatic Frequency Restoration Reserve. Seconds-to-minutes,
  automatic. Restores frequency to 50 Hz.
- **mFRR** — manual Frequency Restoration Reserve. Minutes, manually ordered by
  the TSO. Backstop.
- **Adequacy** — whether enough capacity exists over time to meet demand +
  reserves.
- **Inertia** — rotational energy in spinning synchronous machines that buffers
  frequency changes. Wind/solar inverters provide none.
- **Grid-forming inverter** — an inverter that can set voltage and frequency
  itself (synthetic inertia), unlike conventional grid-following inverters.

### Data / capacity / settlement

- **IGM / CGM / CGMES** — Individual Grid Model (one TSO) / Common Grid Model
  (all merged) / the XML exchange standard for them.
- **ATC / NTC** — Available / Net Transfer Capacity between zones.
- **FB** — Flow-Based capacity calculation; the more advanced method used in the
  Core/CWE region.
- **EIC code** — Energy Identification Code. 16-character ID for market objects.
- **Euphemia** — the algorithm that runs European day-ahead market coupling.
- **ITC** — Inter-TSO Compensation. Compensates transit TSOs for cross-border
  flows.
- **Congestion rent** — the price-spread revenue when power flows across a
  constrained interconnector; goes to the TSOs.
- **Imbalance settlement** — the after-the-fact billing of BRPs for deviations
  from their schedule.
- **Mankala principle** — Finnish model where a power company is owned by its
  customers and sells to them at cost.

---

## Sources used

- ENTSO-E Transparency Platform — https://transparency.entsoe.eu
- ENTSO-E REST API User Guide (PDF, version X.Y) — https://documenter.getpostman.com/view/7009892/2s93JtP3F6
- Open search on google and wikipedia and AI

---

## Changelog

- **2026-05-20** — Initial draft, sections 1–5 filled, others stubbed.
- **2026-05-23** — Sections 1 to 3
- **2026-05-23** — Version 1, All sections filled.
