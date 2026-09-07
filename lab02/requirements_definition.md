Requirements Definition for a simple inventory system:


Functional:

&#x20;- Adding items(picking up)

&#x20;- removing items(dropping)

&#x20;- moving items(dragging items to a different grid slot)

&#x20;- using items(if the item is a consumable)

&#x20;- equipping items

&#x20;- UI

&#x20;- stacking items

&#x20;- Hotbar



Non-functional:
 - UI Design

&#x20;- Item Icons

&#x20;- Item durability



System Design:
	The player first opens the inventory with a keybind. The UI appears onscreen with nothing in the inventory. The player can pick up items and it gets added to the inventory, if there are multiple of the same item it will try to stack them, if the inventory is a portrait design the items will flow from left to right and from top to bottom(first item would be top left, last item would be bottom right). After picking up an item, the player then can move the item within the inventory to different grid spaces, if they want to equip the item they can place the item in the hotbar or press a keybind to equip it. The player can also press a keybind on an item and it will try to use that item. If the player wants to remove the item they would press a certain keybind and the item would be dropped in the game. The player can also close the inventory and continue to play the game.

&#x09;Basically, when an item gets added it gets put into a list and checks the closest grid space to the left in one row. When trying to drop the item, the system calls for the item to be dropped in-game and the item removed from the inventory list making sure there is no way to dupe the item. Using items calls a function within that item(assuming you are using OOP) that adds some effect to your character and removes one of that item that you used. Moving items changes the grid position that is stored in the item within the list and updates the UI. The hotbar is not a second inventory but it helps the player quickly equip an item, the data is provided within the item list. Equipping an item sets the first available hotbar slot as the item you are equipping, otherwise it will just equip the item and do nothing to the hotbar. Durability for certain items are displayed within the inventory and hotbar. 



3-month Development Phase:

|First Half of Month 1|Second Half of Month 1|First half of Month 2|Second Half of Month 2|Month 3|
|-|-|-|-|-|
|Initial inventory system development and item system development|First UI iteration, Adding and removing items from inventory, refining inventory system|Add Moving items, Using Items, and Equiping Items|Further Refinement of Moving, Using, and Equipping items|Playtesting and removing bugs|



