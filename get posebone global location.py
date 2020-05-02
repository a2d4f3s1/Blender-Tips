import bpy
p = bpy.context.active_pose_bone  # Our pose bone
o = bpy.context.object            # Our armature object
global_location = o.matrix_world @ p.matrix @ p.location #以前は*が使えたようだがどこかで変わったらしい
print (global_location)