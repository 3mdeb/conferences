# Conferences

The repository contains slides, white papers and agendas from various events in
which 3mdeb participated in different years. The structure of the repository
consists of folders whose name corresponds to the year in which the conference
was held. Each of these folders contains subfolders whose name corresponds to
the name of the conference at which the company performed in that year. Each of
these subfolders contains materials related to that conference, such as
presentation slides, PDF files and other documents.

The repository also contains a folder named `cfp`, which contains all the Call
for Proposals that the company has produced.

## Structure of the repository

```bash
$ tree -L 2
.
├── 2016
│   └── NetVision
├── 2017
│   └── ECC
├── 2018
│   └── OSFC
├── 2019
│   ├── 36c3
│   ├── ELCE
│   ├── EW
│   ├── LPC
│   ├── OSFC
│   ├── PSEC
│   ├── QubesOS-minisummit
│   └── WebSummit
├── cfp
└── README.md
```

## Events timeline

╔══2016══╗<br>
║ &nbsp;21-23.04&ensp;╠═ [NetVision 2016](2016/NetVision)<br>
╠══2017══╣<br>
║ &nbsp;26-29.10&ensp;╠═ [ECC 2017](2017/ECC)<br>
╠══2018══╣<br>
║ &nbsp;12-15.09&ensp;╠═ [OSFC 2018](2018/OSFC)<br>
╠══2019══╣<br>
║ &nbsp;26-28.02&ensp;╠═ [EW 2019](2019/EW)<br>
╠═══════╣<br>
║ &ensp;&ensp;21.05 &ensp;&ensp;╠═ [QubesOS minisummit2019](2019/QubesOS-minisummit)<br>
╠═══════╣<br>
║ &nbsp;03-06.09&ensp;╠═ [OSFC 2019](2019/OSFC)<br>
╠═══════╣<br>
║ &nbsp;09-11.09&ensp;╠═[LPC 2019](2019/LPC)<br>
╠═══════╣<br>
║ &nbsp;01-03.10&ensp;╠═ [PSEC 2019](2019/PSEC)<br>
╠═══════╣<br>
║ &nbsp;28-30.10&ensp;╠═ [ELCE 2019](2019/ELCE)<br>
╠═══════╣<br>
║ &nbsp;04-07.11&ensp;╠═ [WebSummit 2019](2019/WebSummit)<br>
╠═══════╣<br>
║ &nbsp;27-30.12&ensp;╠═ [36c3 2019](2019/36c3)<br>
╠═══════╣<br>
║ &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; ║<br>
║ &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; ║<br>
║ &nbsp;&ensp;&ensp;TBD&ensp;&ensp;&ensp;║<br>

## Usage

Historically we used [remarkjs](https://github.com/remarkjs/remark) with our
own [remark-remplates](https://github.com/3mdeb/remark-templates), but since
September 2024 we started switching to [slidev](https://sli.dev/).

## How to preview presentation

### slidev

* Install npm manager e.g. [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)
* Use lts version of npm:

```bash
nvm install --lts
nvm use --lts
```

* Install `slidev`:

```bash
npm install @slidev/cli
```

* Host presentations:

```bash
npm run dev -- -p 8000 --remote --force
```

* Open content in browser on http://0.0.0.0:8000

### remarkjs

* Clone repository
* Initialize submodules

  ```bash
  git submodule update --init --recursive --checkout
  ```

* Run local HTTP server e.g.

  ```bash
  python -m http.server
  ```

* Open content in browser on http://0.0.0.0:8000

## Contribution

* Please feel free to create issues for improvement ideas and bugs, as well as
  pull requests to fix any issues.
* If you intend to provide code improvements, please install all dependencies.
* Before pushing code for review, ensure that `pre-commit run --all-files` does
  not return any issues.
