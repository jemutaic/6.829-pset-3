# This is the only file you should need to modify to do this assignment.
#
# The AbrAlg class exposes an API for you to dictate how the next chunk of a
# video should be fetched.
import argparse
parser = argparse.ArgumentParser()
# TODO: Add the required command line arguments to your abr algorithm here (if needed).
# See below for an example. You can specify values for the arguments added here by passing
# them after a *second* '--' delimiter. Example invokation:
# python sim/run_exp.py -- --mm-trace=network/traces/cellular/Verizon1.dat -- --param1=2
parser.add_argument('--param1', type=float, default=1)



class AbrAlg:
  # vid is of type video.Video
  # obj is of type objective.Objective
  def __init__(self, vid, obj, cmdline_args):
    # Use parameters from self.args to define your abr algorithm.
    self.vid = vid
    self.obj = obj
    self.args = parser.parse_args(cmdline_args)
    self.reservoir = 4 # seconds 
    self.cushion = 24 # seconds
    self.prev_rate = None
    self.prev_chunk = None

  ########### Args #####################
  # - 'chunk_index': the index of the chunk to be fetched next, starting at 0.
  # - 'rebuffer_sec': the number of seconds spent rebuffering immediately
  # before the previously watched chunk.
  # - 'download_rate_kbps': The average download rate (in kbps) of the previous chunk
  # - 'buffer_sec': the size of the client's playback buffer (in seconds)
  #
  ########### INITIALIZATION #############
  # Please note that for the first chunk when there is no network feedback yet
  # some of the above arguments take the following default values
  # chunk_index = 0
  # rebuffer_sec = None
  # download_rate_kbps = None
  # buffer_sec = 0

  # Please take special care of the None values above.

  ########### Return Quality ############
  # You should return an index into vid.get_bitrates(), which specifies the
  # bitrate you want to fetch for the next chunk. For example, a return value
  # of 0 indicates that the lowest quality chunk should be fetched next, while
  # len(vid.get_bitrates()) - 1 indicates the highest quality.
  def next_quality(self, chunk_index, rebuffer_sec, download_rate_kbps,
                   buffer_sec):
    r_max_idx = len(self.vid.get_bitrates()) - 1
    r_min_idx = 0

     

    r_max = self.vid.get_bitrates()[r_max_idx]
    r_min = self.vid.get_bitrates()[r_min_idx]


    quality = 0
    rate_plus = None 
    rate_minus = None 

    # TODO: Change the quality to the quality of the bitrate that you want
    # to fetch next.

    # print("download rate: {}".format(download_rate_kbps))
    
    # #update rate_plus
    if self.prev_rate is None:
      rate_plus = self.vid.get_bitrates()[0]
    elif self.prev_rate == r_max:
      rate_plus = r_max
    else:
      for rate in self.vid.get_bitrates():
        if rate > self.prev_rate:
          rate_plus = rate
          break
    
    # # print("ratePlus: {}".format(rate_plus))
    # # update rate_minus
    if self.prev_rate is None:
      rate_minus = self.vid.get_bitrates()[0]
    elif self.prev_rate == r_min:
      rate_minus = r_min 
    else:
      for (i, rate) in enumerate(self.vid.get_bitrates()):
        if rate > self.prev_rate:
          rate_minus = self.vid.get_bitrates()[i-1]
          break



    f_val = self.f(buffer_sec)
    # print("fval: {}".format(f_val))
    # print("buffer_sec: {}".format(buffer_sec))
    # print("Self.reservior: {}".format(self.reservoir))


    #______________________________________#
    # if buffer_sec <= self.reservoir:
    #   # print("MINIMUM INDEX")
    #   quality =  r_min_idx
    # elif buffer_sec >= (self.reservoir + self.cushion):
    #   # print("MAXIMUM INDEX")
    #   quality = r_max_idx
    # else: 
    #   # print("Inside else")
    #   for (i, rate) in enumerate(self.vid.get_bitrates()):
    #     if rate > f_val:
    #       quality = i - 1
    #       break
    # ______________________________________ # 



    #_______________________________________________ #

    # print("rate_plus: {}".format(rate_plus))
    # print("rate_minus: {}".format(rate_minus))
    # print("self.prev_rate: {}".format(self.prev_rate))
    # # print("chunk_index: {}".format(chunk_index))
    # print("rebuffer seconds: {}".format(rebuffer_sec))
    # print("buffer seconds: {}".format(buffer_sec))
    # print("download rate: {}".format(download_rate_kbps))
    # # print("bitrates: {}".format(self.vid.get_bitrates()))
    # print("chunk sizes: {}".format(self.vid.get_chunk_sizes(chunk_index)))
    # print(self.vid.chunks)

    if buffer_sec <= self.reservoir:
      quality = r_min_idx

    elif buffer_sec >= (self.reservoir + self.cushion):
      quality = r_max_idx
    
    elif f_val >= rate_plus:
      for (i, rate) in  enumerate(self.vid.get_bitrates()):
        if rate < f_val:
          quality = i -1 
        elif  f_val < rate:
          # quality = i - 1
          break     
    elif f_val <= rate_minus:
      for (i, rate) in enumerate(self.vid.get_bitrates()):
        if rate > f_val:
          quality = i
          break
    
    else: 
      if self.prev_rate is None:
        quality = 0
      else:
        for (i, rate) in enumerate(self.vid.get_bitrates()):
          if rate ==  self.prev_rate:
            quality = i - 1
            break

    # __________________________________________

    

    # __________________________________
    
    # chunk_sizes = self.vid.get_chunk_sizes(chunk_index)
    # # print("Chunk sizes: {}".format(chunk_sizes))
    # chunk_min = chunk_sizes[0]
    # chunk_max = chunk_sizes[len(chunk_sizes) - 1]

    # # print("")
    # # #update chunk_plus
    # if self.prev_chunk is None:
    #   chunk_plus = chunk_sizes[0]
    # elif self.prev_chunk == chunk_max:
    #   chunk_plus = chunk_sizes[len(chunk_sizes) - 1]
    # else:
    #   for chunk in chunk_sizes:
    #     if chunk > self.prev_chunk:
    #       chunk_plus = chunk
    #       break
    
    # # # print("ratePlus: {}".format(rate_plus))
    # # # update chunk_minus
    # if self.prev_chunk is None:
    #   chunk_minus = chunk_sizes[0]
    # elif self.prev_rate == chunk_min:
    #   rate_minus =  chunk_min
    # else:
    #   for (i, chunk) in enumerate(chunk_sizes):
    #     if chunk > self.prev_chunk:
    #       chunk_minus = chunk_sizes[i-1]
    #       break

      
    # f_val = self.f(buffer_sec, chunk_sizes)
    # # print("f_val: {}".format(f_val))
    # # print("buffers-Sec: {}".format(buffer_sec))

    # # chosen_size_idx = None

    # if buffer_sec <= self.reservoir:
    #   quality =  0
    # elif buffer_sec >= (self.reservoir + self.cushion):
    #   quality = len(chunk_sizes) - 1
    # else:
    #   for (i, size) in enumerate(chunk_sizes):
    #     if size > f_val:
    #       quality = i - 1
    #       break


      


      
      

    # --------------------------------

    # print ("quality: {}".format(quality))
    # print("bitrate: {}".format(self.vid.get_bitrates()[quality]))
    
    if quality < 0:
      quality = 0 
    elif quality > len(self.vid.get_bitrates()):
      quality = len(self.vid.get_bitrates()) - 1
    assert quality >= 0 and quality < len(self.vid.get_bitrates())
  
    self.prev_rate = self.vid.get_bitrates()[quality]
    # self.prev_chunk = chunk_sizes[quality]

    # print("__________________________________________________")
    return quality


  def f(self, b, chunk_sizes=None):
    # _________________________________________

    r_max_idx = len(self.vid.get_bitrates()) - 1
    r_min_idx = 0

    r_max = self.vid.get_bitrates()[r_max_idx]
    r_min = self.vid.get_bitrates()[r_min_idx]

    # gradient = (r_max - r_min)/self.cushion


    # result = (gradient*(b - self.reservoir)) + r_min

    #_____________________________________

  
    # chunk_min = chunk_sizes[0]
    # chunk_max = chunk_sizes[len(chunk_sizes) - 1]

    # gradient = (chunk_max - chunk_min)/self.cushion

    # # print("Gradient: {}".format(gradient))

    # result = (gradient*(b - self.reservoir)) + chunk_min

    # ------------------------------------------

    result = (b - self.reservoir)**3 + r_min

    # ---------------------------------------

    # result = (b - self.reservoir)**2 + r_min

    # ------------------------------------------

    return result
