# demo 08

**Name:** Sagar Patel

**NETID:** sp5894

---

## Question 05
Modify the demo program so the input audio is from the microphone.

**Answer:**

The code was modified in the following section -

`stream = p.open(format = pyaudio.paInt16,`

$\quad \quad \quad$`                channels    = 1,`

$\quad \quad \quad$`                rate        = RATE,`

$\quad \quad \quad$`                input       = True,`

$\quad \quad \quad$`                output      = True )`

`input_bytes = stream.read(1,exception_on_overflow=False)`

...

`for n in range(0,samples):`

$\quad$`    x0, = struct.unpack('h', input_bytes)`

$\quad$`    y0 = b0 * x0 + G * buffer[k]`

$\quad$`    buffer[k] = x0`

$\quad$`    k = k + 1`

$\quad$`    if k >= BUFFER_LEN:`

$\quad \quad$`        k = 0`

$\quad$`    output_bytes = struct.pack('h', int(clip16(y0)))`

$\quad$`    stream.write(output_bytes)`

$\quad$`    input_bytes = stream.read(1,exception_on_overflow=False)`