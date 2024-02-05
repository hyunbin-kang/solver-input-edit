# Solver input editer

This code provide the changing of the CFD solver's input file.

## capavility
This code operate only for the line by line input file.

For example, there are two input files with different format.

```bash
# good code
$flowcon
aoa = 0.0,
aos = 0.0,
mach = 0.5,
Re = 1e6,
```

```bash
# wrong code
$flowcon
aoa    aos    mach     Re
0.0    0.0    0.5      1e6
```

The 1st input file can utilze this code, while the 2nd input file can't.

For the AADL's in-house code, the UMSAPv and IUPAN can use this code, but it doesn's operate in MSAPv's input file.

## User Guide
This source code should be locate in the same directory as the input file.

This is an example for the *Panel.inp*.

```bash
$ python3 main.py
Enter file name : $()
Enter variable name : $()
Enter start boundary : $()
Enter end boundary : $()
Enter boundary step size : $()
```

Type your command into **$()**.

Then this code will make directory for each input, and create modified input file.
