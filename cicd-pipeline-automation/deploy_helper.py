"""Generic deployment helper.

Promotes a built image tag to an environment and polls until the rollout
reports healthy. Illustrative only — status checks are placeholders for a
real mechanism (kubectl rollout status, deploy API, ...).
"""
import argparse
import sys
import time


def tag_image(image: str, tag: str, env: str) -> str:
    release_tag = f"{env}-{tag}"
    print(f"Tagging {image}:{tag} as {image}:{release_tag}")
    return release_tag


def rollout_status(env: str, release_tag: str) -> str:
    # Placeholder for a real status check.
    print(f"Checking rollout of {release_tag} in {env}...")
    return "healthy"


def wait_for_rollout(env: str, release_tag: str, timeout_s: int = 600) -> None:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        if rollout_status(env, release_tag) == "healthy":
            print(f"Rollout {release_tag} healthy in {env}.")
            return
        time.sleep(15)
    sys.exit(f"ERROR: rollout {release_tag} did not become healthy in {timeout_s}s")


def main() -> None:
    parser = argparse.ArgumentParser(description="Promote an image tag to an environment.")
    parser.add_argument("--env", required=True, choices=["staging", "production"])
    parser.add_argument("--tag", required=True, help="Build tag to promote")
    parser.add_argument("--image", default="example-service")
    args = parser.parse_args()

    release_tag = tag_image(args.image, args.tag, args.env)
    wait_for_rollout(args.env, release_tag)


if __name__ == "__main__":
    main()
