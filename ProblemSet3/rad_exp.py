rad=0.0
def radiationExposure(start, stop, step):
	global rad
	if start>=stop:
		rad1=rad
		rad=0.0
		return rad1
	else:
		rad+=(f(start)*step)
		start+=step
		return radiationExposure(start, stop, step)