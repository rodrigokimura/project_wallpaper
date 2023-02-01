# Project Wallpaper

## Summary

Simple wallpaper generator.  
Inspired by [this project](https://github.com/timozattol/wallpaper-generator)

## Usage

`python src/app.py <file_path> <list_of_hex_colors>`

Example:  
`python src/app.py  wallpaper.png '#6272a4' '#8be9fd' '#bd93f9'`

Options:  
You can specify a different screen size (default is 1920x1080):  
`python src/app.py ... --size 3840 2160`
Or a different number of polygons in each side (default is 16x9):  
`python src/app.py ... --resolution 40 30`

You can also control the gradient direction by passing a start and end points:
`python src/app.py ... --start 0 0 --end 3840 2160`

Coordinates are in the format x y, where 0 0 means the top-left corner.

## Examples

Here are some examples and their respective images:

### Three colors gradient
`python src/app.py  example1.png '#6272a4' '#8be9fd' '#bd93f9'`
![Three colors gradient](https://raw.githubusercontent.com/rodrigokimura/project_wallpaper/master/images/example1.png)

### Two colors gradient
`python src/app.py  example2.png '#6272a4' '#1e1e1e'`
![Two colors gradient](https://raw.githubusercontent.com/rodrigokimura/project_wallpaper/master/images/example2.png)

### Less polygons
`python src/app.py  example3.png '#6272a4' '#1e1e1e' --polygons 8 5`
![Less polygons](https://raw.githubusercontent.com/rodrigokimura/project_wallpaper/master/images/example3.png)

### Different direction
`python src/app.py  example4.png '#6272a4' '#1e1e1e' --start 1920 0 --end 0 1080`
![Different direction](https://raw.githubusercontent.com/rodrigokimura/project_wallpaper/master/images/example4.png)

### Different size
`python src/app.py  example5.png '#6272a4' '#1e1e1e' --size 800 600 --end 800 600`
![Different size](https://raw.githubusercontent.com/rodrigokimura/project_wallpaper/master/images/example5.png)


## Dependencies

- Typer
- Pillow
- scikit-spatial
