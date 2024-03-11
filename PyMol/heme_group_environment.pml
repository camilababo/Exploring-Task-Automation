# Get Human Oxyhemoglobin structure
fetch 1HHO
hide everything
show sticks

# Color by carbons & chains
color samarium, elem c and chain A
color antimony, elem c and chain B

# Focus on oxyhemoglobin
select heme, resn HEM and chain A
hide everything, (1HHO)
show sticks, (heme)

# Set distinct visual for iron
select iron, heme and elem fe
show spheres, (iron)
alter iron, vdw=1.2
rebuild iron
color magenta, iron

# Add protein environment around iron
## Find atoms and residues close to iron (distance of 3 angstrom)
select febind, byres(iron expand 3) and (not heme)
show sticks, (febind)
color pink, elem c and heme

# Show amino acid side chains around O2
show lines, (1HHO)
## Select specific residues
select o2bind, resi 29+58+62 and chain A
show sticks, (o2bind)
hide lines, (1HHO)

# Show interaction between His58 & 02
wizard measurement
select sele1, /1HHO/A/A/HIS`58/NE2
select sele2, /1HHO/E/A/OXY`150/O2
distance dist1, sele1, sele2
show dashes, dist1

# Show surrounding molecule
show cartoon, 1HHO
bg_color white
set cartoon_transparency=0.5
hide (name c+o+n)

# Adjust view as wished and set it as default
set_view (\
     0.988667369,   -0.150013700,   -0.005334299,\
     0.026855214,    0.211725995,   -0.976960421,\
     0.147686586,    0.965750337,    0.213355064,\
     0.000000000,    0.000000000,  -36.277606964,\
    40.513000488,   29.277999878,   15.451000214,\
    28.601539612,   43.953674316,  -20.000000000 )

# Define resolution, background and save image
viewport 900, 900
ray
png heme_group_env.png