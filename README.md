# Footstep Detector

An early-stage acoustic sensing project. I noticed that I was able to tell footsteps apart between my family members, so as a first project, I decided that I wanted to create a system that can detect (and eventually localize) footsteps around a house using a singular microphone array. This repo currently covers the first stage: capturing audio and visualizing it to understand what a footstep actually looks like as data, before any classification is attempted.

## What I've built so far

- A Python script that records a short audio clip from a laptop microphone and saves it as a `.wav` file
- A script that loads that clip and plots two views of it:
  - A **waveform** (amplitude over time) — shows loudness spikes where footsteps occurred
  - A **spectrogram** (frequency content over time, via Short-Time Fourier Transform) — shows *which* frequencies were present when, which matters because footsteps have a distinct low-frequency signature compared to background noise
- Both plots stacked with a semi-shared time axis, so a spike in the waveform can be visually cross-referenced against the frequency content at that same moment

This is the foundation for the next stage: collecting labeled clips (footstep vs. not-footstep) and training a small CNN classifier on the spectrograms. I currently have no idea how that will work but I am going to learn as I go.

## My concerns about using AI on this project

I wanted to build something I could understand. My specific concern was that if I leaned on AI to generate the code outright, I'd end up with something that I don't feel like I truly built.

## How I approached it

I split the work into two categories:

- **Setup** (installing packages, fixing environment errors, git commands) — I let AI handle this directly, since there's no real concept to learn from typing `pip install` correctly.
- **The actual signal processing and code logic** — I wrote this myself using official documentation (librosa's docs specifically), and only asked for help when stuck or to review/explain code after I'd written it. This gave me a better insight into how Librosa actually works. I am curious now to see the actual math that is behind the Short-Time Fourier Transform.

When I got stuck, I used VS Code's debugger to step through my own code line by line rather than immediately asking for the fix. I must say, it was a lot more "hands on" than I thought it would be, so admittedly, it made some major changes to a few parts of the code.

## What I've learned

- How `librosa.load()` reads an audio file into a raw waveform array (`y`) and sample rate (`sr`)
- What a Short-Time Fourier Transform actually does: instead of one FFT over an entire clip (which loses timing information), it slides a window across the signal.
- Why raw STFT magnitude data needs to be converted to a decibel scale before it's visually interpretable — the dynamic range of raw magnitude values is too large to show meaningful detail without it
- Basic git workflow: initializing a repo, staging, committing, connecting to a remote, and resolving a push conflict caused by unrelated commit histories

## What's next

1. **Collect a labeled dataset** — record and label a batch of clips as "footstep" vs. "not footstep" (silence, talking, background noise)
2. **Train a small CNN** on spectrograms of these clips to classify footstep vs. not-footstep
3. **Move to real-time detection** — stream from the mic continuously and classify on a rolling basis
4. **Deploy on dedicated hardware** — move from laptop testing to a Raspberry Pi + ReSpeaker mic HAT. I asked claude and it said a single mic array would not be physically capable of distinguishing floors. I do struggle personally to do this, but using first principles thinking (similar to that of Elon wanting to stick to only cameras for self-driving - because humans don't use LIDAR) I want to attempt to use 2 mikes only to start.
5. **Evaluate honestly** — report detection accuracy vs. distance/background noise, and false positive rate.

## Output Example

This is an example of myself and my brother creating a copiuos amount of background noise while playing a 8500Hz frequency from an app on my phone. Although quite obvious, I found it interesting to see that the frquency graph captured a sort of 'hidden data point' that the waveform didn't. Not a groundbreaking discovery by any means but it peaked my interest.

<img width="638" height="477" alt="Screenshot 2026-08-20 at 2 05 06 PM" src="https://github.com/user-attachments/assets/165d7851-b09a-4bf9-9f03-973f0f1eb452" />

## Closing Thoughts

It's August 20th 2026, I feel like time is flying at the moment. yesterday I polished off the end of Player of Games from the Culture Series books by Ian M. Banks, and a quote by my favorite character in the book (who I shall not reveal the name of, as it would be a massive spoiler.)  says: "Does identity matter anyway? I have my doubts. We are what we do, not what we think. Only the interactions count. (There is no problem with free will here; that's not incompatible with believing your actions define you). What is free will anyway? Chance. The random factor. If one is not ultimately predictable, then of course that's all it can be. I get so frustrated with people who can't see this!"  when I see other people with incredible projects, I often find myself thinking, "If only people could see what I think," because I think they would be more impressed by that than what I've built. That's why, when I saw this quote, it sort of lit a fire under my bum. Although this project is not impressive by any means, it's done and finished. I have a result to show for it, and so I am pleased.
