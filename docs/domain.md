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
The "Open questions" section is the to-learn queue.

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

<!-- your answer -->

### Intraday market (ID)

<!-- your answer -->

### Balancing market (BAL)

<!-- your answer -->

**Plus the reserves:** what's the difference between FCR, aFRR, mFRR?
Order them from fastest activation to slowest, and write one line
each on what triggers them.

<!-- your answer -->

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

<!-- your scenario -->

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

<!-- your answer -->

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

<!-- your paragraph -->

---

## 8. Bidding zones and EIC codes

**Prompts:**

- What is a bidding zone? Why doesn't every country = exactly one zone?
- Give an example of a country split into multiple zones (and why).
- What's an EIC code? What does the FI bidding zone code look like?
- Why does the API use these codes instead of human-readable names?

<!-- your answer -->

---

## 9. The data exchange layer — IGM, CGM, CGMES

**Prompts:**

- What is an IGM? What does it contain (just wires? or also operational
  state?)
- What's the CGM, and how is it built from IGMs?
- What's CGMES, in one line?
- Why does ENTSO-E need this? (Hint: cross-border capacity calculation,
  security analysis across the whole synchronous area.)

<!-- your answer -->

---

## 10. The Finnish landscape — who's who

Fill in what you know. For each, note: role, ownership type, rough size,
data needs you'd guess they have.

### Finland's TSO

- **Fingrid** — <!-- your notes -->

### Top Finnish DSOs

- Caruna — <!-- your notes -->
- Elenia — <!-- your notes -->
- Helen Sähköverkko — <!-- your notes -->
- Others worth knowing: <!-- list -->

### Major Finnish generators

- Fortum — <!-- your notes -->
- Helen — <!-- your notes -->
- TVO (Teollisuuden Voima) — <!-- your notes -->
- Pohjolan Voima (PVO) — <!-- your notes -->
- Others: <!-- list -->

### BESS operators & aggregators active in Finland / Nordics

- Ingrid Capacity — <!-- your notes -->
- Sympower — <!-- your notes -->
- Capalo AI — <!-- your notes -->
- Forus — <!-- your notes -->
- Others you've heard of: <!-- list -->

### Power exchange

- Nord Pool — <!-- your notes -->

### Regulator

- Energiavirasto — <!-- your notes -->

---

## 11. Why this dataset for the project

(Comes from §1 / §2 of our roadmap conversation. Write this in your own
words — it's the elevator pitch.)

**Prompts:**

- Who is the imagined stakeholder for the platform I'm building?
- What pain are they in today, without my platform?
- What does "good" look like for them — what does my platform enable?
- Why is ENTSO-E data the right source for that stakeholder, vs alternative
  data sources?
- What's interesting about this data engineering-wise (volume, schema,
  velocity, weird quirks)?

<!-- your answer -->

---

## 12. Glossary

Define each in your own words. If you can't, that goes under §13.

### Organisations & roles

- ENTSO-E
- TSO
- DSO
- NEMO
- BRP
- BSP
- ACER
- Energiavirasto
- Nord Pool
- EPEX SPOT

### Market / time concepts

- Day-ahead market (DA)
- Intraday market (ID)
- Balancing market (BAL)
- MTU (Market Time Unit)
- Gate closure
- Bidding zone
- Synchronous area

### Operational / technical

- N-1 criterion
- FCR, aFRR, mFRR
- Adequacy
- Inertia / synchronous inertia
- Frequency containment
- Grid-forming inverter (one-liner, optional)

### Data / capacity / settlement

- IGM, CGM, CGMES
- ATC, NTC, FB (flow-based) capacity
- EIC code
- Euphemia (the algorithm)
- ITC (Inter-TSO Compensation)
- Congestion rent
- Imbalance settlement
- Mankala principle (Finnish quirk — look this one up)

---

## 13. Open questions / things to research more

A running list of things I haven't fully understood yet. Don't fake
clarity — write the genuine question.

- <!-- e.g. "How exactly does flow-based capacity calculation differ from NTC?" -->
- <!-- e.g. "Why are negative prices increasing in 2025–2026? Mechanism?" -->
- <!-- e.g. "What's a grid-forming inverter and why did Iberia care?" -->
- <!-- add your own -->

---

## 14. Sources I've used

Keep this list honest. Even just titles + URLs.

- ENTSO-E Transparency Platform — https://transparency.entsoe.eu
- ENTSO-E REST API User Guide (PDF, version X.Y) — <!-- link -->
- <!-- add others as you read them -->

---

## Changelog

- **YYYY-MM-DD** — Initial draft, sections 1–5 filled, others stubbed.
- <!-- subsequent entries -->
