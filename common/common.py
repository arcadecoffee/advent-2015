def print_progress_bar(total_steps: int = 100, current_step: int = 0):
    if current_step == total_steps:
        print(f'[{"=" * 20}] 100%')
    else:
        progress = int(20 * current_step / total_steps)
        print(f'[{"=" * progress}>{"-" * (19 - progress)}] {progress * 5}%', end='\r')