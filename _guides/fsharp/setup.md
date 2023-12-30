---
layout: page
title: Setup F#
date: 2023-04-01
permalink: /guides/fsharp/intro/setup/
---

First up, create a new folder to start exploring.  Then, create the following file `.devcontainer/devcontainer.json`

```json-comments
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/dotnet-fsharp
{
	"name": "F# (.NET)",
	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
	"image": "mcr.microsoft.com/devcontainers/dotnet:0-6.0-bullseye",

	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},

	// Configure tool-specific properties.
	"customizations": {
		// Configure properties specific to VS Code.
		"vscode": {		
			// Add the IDs of extensions you want installed when the container is created.
			"extensions": [
				"Ionide.Ionide-fsharp",
				"ms-dotnettools.csharp"
			],
            "settings": {
                "FSharp.dotnetRoot": "/usr/share/dotnet"
            }
		}    
	}

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],

	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "dotnet restore",

	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	// "remoteUser": "root"
}
```

VS Code should prompt you to reload in dev container.  

After reloading VS Code, you can open a terminal and startup the F# interactive with:  


```bash
dotnet fsi
```

Then, tryout a simple command:

```fsharp
let name = "world"
printfn "Hello %s" name;;
```

Then, you should get the following output:

```
> let name = "world"
- printfn "Hello %s" name;;
Hello world
val name: string = "world"
val it: unit = ()
```


> Let's talk about [values](/guides/fsharp/intro/value).