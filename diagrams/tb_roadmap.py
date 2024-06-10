#!/usr/bin/env python3


from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

version = "v0.1"
date = "May 2024"

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/timeline.json", show_marker=False)
roadmap.set_title("TrenchBoot roadmap")
roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-06-01", number_of_items=12)

ongoing = roadmap.add_group("Ongoing work", font_size=26)
ongoing.add_task("Package repositories", "2024-06-01", "2024-07-31", style="rounded", fill_colour="#34A853", font_size=23)
ongoing.add_task("DRTM assessment tool", "2024-07-01", "2024-08-31", style="rounded", fill_colour="#ADD8E6", font_size=23)
ongoing.add_task("QubesOS Security Report extension", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14", font_size=23)
ongoing.add_task("fwupd HSI extension", "2024-09-01", "2024-11-30", style="rounded", fill_colour="#EA4335", font_size=23)

phase5 = roadmap.add_group("Phase 5", font_size=26)

phase5.add_task("Xen Secure Launch on EFI system", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#34A853", font_size=23)
phase5.add_task("TrenchBoot AEM Compatibility Test Suite", "2025-03-01", "2025-06-30", style="rounded", fill_colour="#FD7E14", font_size=23)

roadmap.set_footer(f"TrenchBoot ongoing work and future plans | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("img/tb_roadmap.png")
