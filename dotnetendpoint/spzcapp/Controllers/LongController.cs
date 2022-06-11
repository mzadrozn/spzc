using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Threading;

namespace zzsnapp.Controllers
{
  [ApiController]
  [Route("[controller]")]
  public class LongController : ControllerBase
  {
    private readonly ILogger<LongController> _logger;
    private readonly int _sleepTime = 3500;
    public LongController(ILogger<LongController> logger)
    {
      _logger = logger;
    }

    [HttpGet(Name = "GetLong")]
    public String Get()
    {
      Thread.Sleep(_sleepTime);
      return "{\"from\": \"dotnetAPI\", \"message\": \"long request processed\"}";
    }
  }
}
