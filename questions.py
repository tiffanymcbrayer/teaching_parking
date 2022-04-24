questions2 = {
    "0": {
        'ord': 0,
        "name": "Forwards Parking",
        "steps": [[1, "Drive forward until the :carterms: lines up with the parking line"],
                  [2,
                      "Turn the wheel to your :directions: and move forward into space"],
                  [3, "Once you are centered in the spot, straighten the wheel and move up to the line"]],

        "answers": {1: 'mirror',
                    2: 'right'}
    },
    "1": {
        'ord': 1,
        "name": "Reverse Parking",
        "steps": [[1, "Drive forward until the :carterms: lines up with the parking line (keep close to the space)"],
                  [2,
                      "Turn the wheel to your :directions: and go forward until you see edge of parking line in left mirror"],
                  [3,
                      "Straighten the wheel until you align your :directions: mirror with the edge of the car to your right"],
                  [4,
                      "Turn the wheel to the :directions: and reverse until you are centered in the spot"],
                  [5, "Once you are centered in the spot, straighten the wheel and move up to the line"]],
        "answers": {1: 'mirror',
                    2: 'left',
                    3: 'right',
                    4: 'right'}
    },
    "2": {
        'ord': 2,
        "name": "Angled Parking",
        "steps": [[1, "Drive forward until the :carterms: lines up with the parking line"],
                  [2,
                      "Turn the wheel to your :directions: and go forward into space"],
                  [3, "Once you are centered in the spot, straighten the wheel and move up to the line "]],

        "answers": {1: 'mirror',
                    2: 'left'}
    },
    "3": {
        'ord': 3,
        "name": "Parallel Parking",
        "steps": [[1, "Drive forward until your car is in line with :roadterms: (keep a reasonably close distance to the car)"],
                  [2,
                      "Turn the wheel all the way to your right and reverse until you can see the :roadterms: through the mirror "],
                  [3,
                      "Straighten out the wheel and back in until you align your right mirror with :roadterms: in front"],
                  [4,
                      "Turn the wheel :directions: and back up until you have no more space"],
                  [5, "Once you are centered in the spot, straighten the wheel and move up until you are in the middle of the spot"]],
        "answers": {1: 'the car next to you',
                    2: 'parking line corner',
                    3: 'the other car',
                    4: 'left'}
    }
}

directions = ['left', 'right']
carterms = ['mirror', 'front wheel', 'rear wheel']
roadterms = ['parking line corner', 'parking line end',
             'the car next to you', "the other car's bumper"]
