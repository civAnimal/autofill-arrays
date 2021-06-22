## AutoFill Arrays For Sublime Text

This plugin allows you to fill `Arrays` with lists of interesting/meaningful words or numbers by typing just a few keys. You have a choice to pick from several available categories. It works equally well in all mainstream programming languages, like `Python`, `Javascript`, `Java`, `C`, `C++`, `C#`, `Lua`, `Ruby`, etc. You could also use it with other array-like collection objects/types, like `List`, `Set`, `Tuple`, etc.


![DEMO](https://github.com/civAnimal/autofill-arrays/blob/main/demo.gif)


### Available Categories

`Flowers`, `Fruits`,   `Colors`, `Birds`,   `Animals`, `Gems`,   `Directions`,
`Insects`, `Fish`,     `Foods`,  `Drinks`,  `Months`,  `Days`,   `Vegetables`,
`Planets`, `Elements`, `Metals`, `Greeks`,  `Romans`,  `Trees`,  `Languages`,
`Oceans`,  `Seas`,     `Rivers`, `Seasons`, `Zodiacs`, `Numbers`


### Examples

 Text Entered  |  Result
-------------- | --------------------------------------------------------------------
 `flwa`        | `"Rose", "Dahlia", "Magnolia", "Tulip", "Daisy"`
 `frua`        | `"Apple", "Mango", "Avocado", "Cherry", "Pomegranate"`
 `bira`        | `"Dove", "Eagle", "Raven", "Penguin", "Owl"`
 `fisa`        | `"Shark", "Whale", "Dolphin", "Salmon", "Trout"`
 `trea`        | `"Oak", "Maple", "Pine", "Sycamore", "Willow"`
 `colp`        | `"Red", "Yellow", "Blue"`
 `colr`        | `"Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"`
 `elma`        | `"Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"`
 `numof`       | `371, 373, 375, 377, 379, 381, 383, 385, 387, 389`
 `numpre`      | `101, 103, 107, 109, 113, 127, 131, 137, 139, 149`


### Prefix Feature

* From ver 2.0, prefix feature has been introduced to help address the issue of undue clutter. Default prefix is `voc`. This is completely configurable. If you want the old/direct invocation behaviour back, simply set the prefix to `""` empty string.

* Menu command to change prefix: _Preferences_ → _Package Settings_  → _AutoFill Arrays_  → _Change Prefix_

* After saving changes, the plugin must be reloaded for those changes to take effect.

* Menu command to reload plugin: _Preferences_ → _Package Settings_  → _AutoFill Arrays_  → _Reload Plugin_


### Tips

* Type only a few letters of the desired category. If you don't see Sublime Text's AutoComplete System responding to your typing, then you could activate it manually by pressing `ctrl + space`.

* Most categories comprise several short (5 elements) and long (>= 10 elements) lists. Explore them and incorporate them in your workflow accordingly.


### Installation

* Download the plugin (or clone this repository).
* After extraction, copy `autofill_arrays` folder to Sublime Text's _Packages_ folder.
* You can locate this folder from Sublime Text by using the menu command: _Preferences_ → _Browse Packages_.
* You could start using this plugin straight away; no restart required.


### Notes

* Most of the data has been sourced, with thanks, from https://www.wikipedia.org
* Released under ... Creative Commons License (CC BY-SA).


### Feedback & Comments

* Email:     civanimal@gmail.com
* Twitter:  `civAnimal`


Copyright (c) 2021 civAnimal
