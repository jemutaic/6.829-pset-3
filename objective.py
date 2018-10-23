# A class that expresses the main QoE metric that your ABR algorithm will be
# evaluated on. An instance of this class will be passed into your AbrAlg
# constructor. You may call any of its functions at any point.

class Objective:
    # - `pquals` is a dictionary mapping bitrate (kbps) to perceptual quality (on
    # a scale of 0 - 100.
    # - `startup` is the penalty for each second spent waiting for the
    # first chunk to buffer.
    # - `rebuf` is the penalty for each second spent rebuffering after the first
    # chunk.
    # - `smooth` is the penalty for changes in bitrate.
    # All penalties are non-negative floating point numbers.
    def __init__(self, pquals, startup, rebuf, smooth):
        self._perceptual_qualities = pquals
        self._startup_penalty = startup
        self._rebuf_penalty = rebuf
        self._smooth_penalty = smooth

    def perceptual_qualities(self):
        return self._perceptual_qualities

    def startup_penalty(self):
        return self._startup_penalty

    def rebuf_penalty(self):
        return self._rebuf_penalty

    def smooth_penalty(self):
        return self._smooth_penalty

    # Computes the QoE for any chunk (except the first), given:
    #  - `cur_bitrate`: the bitrate of that chunk
    #  - `prev_bitrate`: the bitrate of the previous chunk
    #  - `rebuf_sec`: the number of seconds spent waiting for this chunk to
    #  rebuffer. Note that rebuffering penalties are assigned to the chunk
    #  immediately following a rebuffering event.
    def qoe(self, cur_bitrate, prev_bitrate, rebuf_sec):
        pq_cur = self._perceptual_qualities[cur_bitrate]
        pq_prev = self._perceptual_qualities[prev_bitrate]
        return pq_cur \
                - self._rebuf_penalty * rebuf_sec \
                - self._smooth_penalty(abs(pq_prev - pq_cur))

    # Computes the QoE for the first chunk in a video, given:
    # - `cur_bitrate`: the bitrate of the first chunk
    # - `delay_sec`: The number of seconds it took to fetch the first chunk and
    # start playing the video.
    def qoe_first_chunk(self, cur_bitrate, delay_sec):
        pq_cur = self._perceptual_qualities[cur_bitrate]
        return pq_cur - self._startup_penalty * delay_sec

