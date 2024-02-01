#!/usr/bin/env python3


from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

# Old AMD processors

roadmap_old = Roadmap(1600, 1000, colour_theme="timeline.json", show_marker=False)
roadmap_old.set_title("AMD processors timeline")
roadmap_old.set_timeline(TimelineMode.YEARLY, start="2011-11-01", number_of_items=5)

embedded = roadmap_old.add_group("Embedded")

embedded.add_task("Bobcat", "2011-05-01", "2021-06-01", style="rounded", fill_colour="#EA4335")
embedded.add_task("Puma", "2014-04-01", "2023-10-01", style="rounded", fill_colour="#34A853")

mobile = roadmap_old.add_group("Mobile")

mobile.add_task("Piledriver", "2012-05-01", "2015-02-14", style="rounded", fill_colour="#ADD8E6")

server = roadmap_old.add_group("Server")

server.add_task("Bulldozer", "2011-11-01", "2014-11-01", style="rounded", fill_colour="#EA4335")
server.add_task("Piledriver", "2012-11-01", "2015-11-01", style="rounded", fill_colour="#34A853")

roadmap_old.draw()
roadmap_old.save("amd_processors_old.png")

# Zen processors

roadmap_zen = Roadmap(1600, 1000, colour_theme="timeline.json", show_marker=False)
roadmap_zen.set_title("AMD Zen processors timeline")
roadmap_zen.set_timeline(TimelineMode.YEARLY, start="2019-01-01", number_of_items=9)

mobile = roadmap_zen.add_group("Mobile")

mobile.add_task("Picasso (Zen+)", "2019-01-06", "2022-01-06", style="rounded", fill_colour="#34A853")
mobile.add_task("Cezanne (Zen3)", "2021-01-12", "2024-01-12", style="rounded", fill_colour="#ADD8E6")
mobile.add_task("Mendocino (Zen2)", "2022-09-20", "2025-09-20", style="rounded", fill_colour="#EA4335")
mobile.add_task("Phoenix (Zen4)", "2023-05-03", "2026-05-03", style="rounded", fill_colour="#34A853")
mobile.add_task("Glinda (Hawk Point? Zen4?)", "2024-03-01", "2027-03-01", style="rounded", fill_colour="#ADD8E6")

server = roadmap_zen.add_group("Server")
server.add_task("Genoa (Zen4)", "2022-11-10", "2025-11-10", style="rounded", fill_colour="#34A853")

roadmap_zen.draw()
roadmap_zen.save("amd_processors_zen.png")
