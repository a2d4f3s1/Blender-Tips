import bpy
###################################
HookBoneName = 'bone01'
###################################

Arm = bpy.context.object  # Get current armature
CurrentBone = bpy.context.active_pose_bone  # Get current bone
HookBone = Arm.pose.bones[HookBoneName]  # Get hook bone

CurrentBone_GlobalLocation = Arm.matrix_world @ CurrentBone.head  # Global coordinates of CurrentBone
HookBone_GlobalLocation = Arm.matrix_world @ HookBone.head  # Global coordinates of HookBone
RelativeCoordinate = CurrentBone_GlobalLocation - HookBone_GlobalLocation  # Relative coordinates

print(CurrentBone_GlobalLocation)
print(HookBone_GlobalLocation)
print(RelativeCoordinate)
