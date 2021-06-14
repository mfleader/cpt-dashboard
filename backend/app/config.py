from vyper import v
from environs import Env
from marshmallow.validate import Length
from typing import Optional


def get_config():
	# not yet sure if we want to have elasticsearch config file path override
	# option
	# env = Env()
	# env.read_env()
	# if os.getenv('OCPPERF_SERVER_CONFIG') is not None:
	# 	env.str(
	# 		'OCPPERF_SERVER_CONFIG',
	# 		validate=Length(min=1),
	# 		subset=Optional
	# 	)
	v.set_config_name('ocpperf')
	v.add_config_path('.')
	v.read_in_config()
	return v
