# L-System 2D Renderer

## Demo/Saved Rules
- Simple "Cyber Tree" : Rule `"F": "FF[-F+F][+F-F]"` Axiom `"F"` Step 60
- "Eye" : Rule `"F": "FFF[-F+F--FF+][+F-F++FF-]FFF++"` Axiom `"F"` Step 30
- Sierpinski Triangle : Rules `"F": "F-G+F+G-F"` `"G": "GG"` Axiom `"F-G-G"` Step 120
- Cyber Something : Rules `"F": "GG[F+F-F]+GG[F-F+F]+GG", "G": "GG"` Axiom `"F++GGF--GGF++GG"` Step 60
- Cyber Triangle Thing : Rules `"F": "GG[F+F-F]+GG[F-F+F]+GG", "G": "--GG++"` Axiom `"FGFGFG"` Step 60
- Cyber Triangle Other : Rules `"F": "GGXX[F+F-F]+GXG[F-F+F]+GG", "G": "--GG++"` Axiom `"FGFGFG"` Step 60
- Virus : Rules `"F": "[G[+F][-F]], "G": "GG"` Axiom `"FG+FG+FG+FG+FG+FG"`Step 60


## v1.0
To use: Input the rules into each related sector of the dictionary (i.e F to F, G to G), the axiom to the axiom variable and the step to the step variable.
Then run the program.