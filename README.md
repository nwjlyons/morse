#Sending morse code using the amplitude of a sound wave

Open three terminals

1. `sleep 3 && ./encoder.py "Hi" | ./speaker.py`
2. `sleep 1 && timeout --signal=2 190 ./mic.py`
3. `./decoder.py`

At the moment it takes two seconds to transmit one binary digit.

Use `./encoder.py "Hi" | wc -m` to calculate how many binary digits there are. Then mulitply by two to get the length of time the transmission will take.

##Installation

- Create virtualenv `mkvirtualenv morse`
- Install requirements `pip install -r requirements.txt`