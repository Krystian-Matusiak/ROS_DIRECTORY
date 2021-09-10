#!/usr/bin/zsh

xacro model.xacro > model.urdf
gz sdf -p model.urdf > model.sdf
