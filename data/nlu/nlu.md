## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:search
- Search for a [card](product) please
- Search [cards]{"entity": "product", "value": "card"}
- Please search for [cards]{"entity": "product", "value": "card"}
- Search [card](product)
- Find a [card](product)
- I'm looking for a specific [card](product)
- I want to search [sets]{"entity": "product", "value": "set"}
- I want to search for a [set](product)
- Search for a [set of cards]{"entity": "product", "value": "set"}
- I would like to perform a search
- Search for something
- for a [card](product)
- [card](product)
- [cards]{"entity": "product", "value": "card"}
- [set](product)
- [sets]{"entity": "product", "value": "set"}
- search for [cards]{"entity": "product", "value": "card"}
- search please
- search for something
- mmmm. [cards]{"entity": "product", "value": "card"}
- mmmm. [sets]{"entity": "product", "value": "set"}

## intent:describe_card
- It's a [blue](card_color) card
- It's [red](card_color)
- It's [white](card_color) colored
- It's [green](card_color) one
- The color is [white](card_color)
- The color is [black](card_color)
- It has [black](card_color) color
- It's a [colorless](card_color) card
- It does not have a color, it's a [colorless](card_color) card
- It's a [multicolor](card_color) card
- It's an [abzan](card_color) card
- It's a [multicolored]{"entity": "card_color", "value": "multicolor"} one
- It's a [multicoloured]{"entity": "card_color", "value": "multicolor"} card
- Looking for a [black](card_color) [enchantment](card_type)
- Looking for an [instant](card_type) card
- Hmm it's an [enchantment](card_type)
- Hmm it's also a [creature](card_type) card, with color [green](card_color)
- The card is an [artifact](card_type)
- Check for [artifacts]{"entity": "card_type", "value": "artifact"}
- [creatures]{"entity": "card_type", "value": "creature"}
- I know it's a [sorcery](card_type) card
- look for [sorceries]{"entity": "card_type", "value": "sorcery"}
- look for [instants]{"entity": "card_type", "value": "instant"} please
- look for [instants]{"entity": "card_type", "value": "instant"} please, with [golgari](card_color) colors
- What I know: it's a [blue](card_color) [sorcery](card_type)
- Get [lands]{"entity": "card_type", "value": "land"} first, with color [blue](card_color)
- The card type is [instant](card_type)
- [white](card_color) [enchantment](card_type)
- [multicolor](card_color) [enchantments]{"entity": "card_type", "value": "enchantment"}
- It's a [land](card_type), the rarity is [common](card_rarity)
- It's a [rare](card_rarity) [creature](card_type)
- Well, it's a [mythic](card_rarity) [creature](card_type) for starters
- I remember it's an [uncommon](card_rarity) [black](card_color) [instant](card_type) card
- I believe it's a [common](card_rarity) card, don't know the color
- It's a [legendary]{"entity": "card_subtype", "value": "legend"} [creature](card_type)
- A [legend](card_subtype) card, [black](card_color) color
- Give me [legend](card_subtype) cards
- I'm looking for a [legendary]{"entity": "card_subtype", "value": "legend"} [goblin](card_creature_type)
- Find me a [black](card_color) [horror](card_creature_type) card
- Find me [green](card_color) [beast](card_creature_type) cards please
- It's a [werewolf](card_creature_type) [creature](card_type)
- It's a [serpent](card_creature_type)
- I'm looking for all [soldier](card_creature_type) cards, any color
- I'm looking for all [angel](card_creature_type) cards, no color preference

## intent:random_card
- show me a random card
- get me a random card
- get me a random card please
- random card
- any card!

## intent:chitchat/thank
- Thanks!!
- thanks for that
- thanks for this
- thank you
- thanks a lot
- thank mr. bot

## intent:chitchat/challenge_bot
- Are you a bot?
- Are you a robot?
- You're a bot
- Are you human?
- Are you a person?
- Are you real?
- Who are you?
- What are you?

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- lalala

## intent:deny
- no
- never
- I don't think so
- not really
- nope

## synonym:artifact
- artifacts

## synonym:card
- cards

## synonym:creature
- creatures

## synonym:enchantment
- enchantments

## synonym:instant
- instants

## synonym:land
- lands

## synonym:legend
- legendary

## synonym:multicolor
- multicolored
- multicoloured

## synonym:set
- sets
- set of cards

## synonym:sorcery
- sorceries

## lookup:lookup_colors.txt
  data/lookup_colors.txt

## lookup:lookup_creatures.txt
  data/lookup_creatures.txt
