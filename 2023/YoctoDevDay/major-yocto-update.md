Title:
Updates of Yocto-Based Projects: Effective strategies for ongoing maintenance

Description:
Continuously updating the source code of Yocto-based projects is crucial for
various reasons. It encompasses vital aspects such as patching security
vulnerabilities by incorporating newer application versions that address
identified and resolved CVEs, as well as minimizing technical debt through the
integration of novel functionalities. Leveraging the Yocto Project's stable
release cycle empowers developers to maintain up-to-date components within the
operating system. Additionally, its comprehensive monitoring capabilities
facilitate ongoing system composition analysis, enabling prompt error detection
in individual components.

In this session, we will delve into effective strategies for seamlessly updating
Yocto-based projects, exploring best practices, tools, and techniques that
ensure efficient maintenance and sustainable project evolution. The main
objective is to provide an understanding of the entire upgrade process, covering
key aspects such as updating individual components, implementing
release-specific modifications to Yocto and conducting thorough testing of the
resulting image to ensure no regression of functionality. By the end of this
presentation, every participant will be well aware of the challenges involved in
upgrading a system.

To bring these concepts to life, we will illustrate the topics through a real
example: the process of updating a system designed for RTE [1][2] devices.
Specifically, we will explore the transition from the Dunfell to Kirkstone Yocto
releases, representing the shift between the last two LTS versions. This
tangible demonstration will provide participants with a practical perspective
and actionable knowledge, empowering them to confidently undertake their own
system updates.

[1] https://github.com/3mdeb/meta-rte/
[2] https://docs.dasharo.com/transparent-validation/rte/introduction/
